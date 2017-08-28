import numpy as np
import pandas as pd
import lightgbm as lgb
import gc

print "Loading data"

train_data = pd.read_csv("train_2016.csv")
prop_data = pd.read_csv("properties_2016.csv")

for c, dtype in zip(prop_data.columns, prop_data.dtypes):
    if dtype == np.float64:
        prop_data[c] = prop_data[c].astype(np.float32)


df_train = train_data.merge(prop_data, how="inner", on="parcelid")

x_train = df_train.drop(['parcelid', 'logerror', 'transactiondate',
                         'propertyzoningdesc', 'propertycountylandusecode'],
                        axis=1)
y_train = df_train['logerror'].values
print  x_train.shape, y_train.shape

train_cols = x_train.columns

for c in x_train.dtypes[x_train.dtypes == object].index.values:
    x_train[c] = (x_train == True)

del df_train
gc.collect()

split = 90400 #earlier - 90K

x_train, y_train, x_valid, y_valid = x_train[:split], y_train[:split], x_train[split:], y_train[split:]
x_train = x_train.values.astype(np.float32, copy=False)
x_valid = x_valid.values.astype(np.float32, copy=False)

d_train = lgb.Dataset(x_train, label=y_train)
d_valid = lgb.Dataset(x_valid, label=y_valid)

params = {}

params['max_bin'] = 30 # earlier 10
params['learning_rate'] = 0.0021 # shrinkage_rate
params['boosting_type'] = 'gbdt'
params['objective'] = 'regression'
params['metric'] = 'l2'          # or 'mae'
params['sub_feature'] = 0.5      # feature_fraction
params['bagging_fraction'] = 0.85 # sub_row
params['bagging_freq'] = 40
params['num_leaves'] = 600        # num_leaf - earlier 512
params['min_data'] = 500         # min_data_in_leaf - earlier 600
params['min_hessian'] = 0.05     # min_sum_hessian_in_leaf

watchlist = [d_valid]
clf = lgb.train(
    params, d_train, 400, watchlist, verbose_eval=True
)

del d_train, d_valid; gc.collect()
del x_train, x_valid; gc.collect()

print "Prepare for the prediction ..."
sample = pd.read_csv('sample_submission.csv')
sample['parcelid'] = sample['ParcelId']

df_test = sample.merge(prop_data, on='parcelid', how='inner')

del sample, prop_data; gc.collect()

x_test = df_test[train_cols]
del df_test; gc.collect()

for c in x_test.dtypes[x_test.dtypes == object].index.values:
    x_test[c] = (x_test[c] == True)

x_test = x_test.values.astype(np.float32, copy=False)

print "Start prediction"
clf.reset_parameter({"num_threads":1})
p_test = clf.predict(x_test)

print("Writing result into file ...")
sub = pd.read_csv('sample_submission.csv')

for c in sub.columns[sub.columns != 'ParcelId']:
    sub[c] = p_test

sub.to_csv('lgb_tuned_params_2.csv', index=False, float_format='%.4f')

print("Program ended")