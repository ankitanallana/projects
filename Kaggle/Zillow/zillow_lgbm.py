import pandas as pd
import lightgbm as lgb
import numpy as np
import gc
from sklearn.model_selection import train_test_split

print('Load data...')
log_values = pd.read_csv('train_2016.csv')
train_values = pd.read_csv('properties_2016.csv')
test_data = pd.read_csv('sample_submission.csv')

train_data = train_values
merged_data = train_data.merge(log_values, how='inner',
                               on='parcelid')

object_cols = merged_data.dtypes[merged_data.dtypes==object].index.values

for o in object_cols:
    merged_data[o] = (merged_data[o]==True)

gc.collect()

train_data, valid_data = train_test_split(merged_data,
                                          test_size=0.1,
                                          random_state=55)

y_values_train = train_data.iloc[:, 58:59]
x_values_train = train_data.iloc[:, 0:58]

y_values_valid = valid_data.iloc[:, 58:59]
x_values_valid = valid_data.iloc[:, 0:58]

lgb_train = lgb.Dataset(x_values_train, y_values_train['logerror'])
lgb_valid = lgb.Dataset(x_values_valid, y_values_valid['logerror'], reference=lgb_train)

"""params = {}
params['learning_rate'] = 0.1
params['boosting_type'] = 'gbdt'
params['objective'] = 'regression'
params['metric'] = 'mae'
params['feature_fraction'] = 0.6
params['num_leaves'] = 50
params['min_data'] = 500
params['min_hessian'] = .1"""

params = {}
params['max_bin'] = 10
params['learning_rate'] = 0.0021 # shrinkage_rate
params['boosting_type'] = 'gbdt'
params['objective'] = 'regression'
params['metric'] = 'l2'          # or 'mae'
params['sub_feature'] = 0.5      # feature_fraction
params['bagging_fraction'] = 0.85 # sub_row
params['bagging_freq'] = 40
params['num_leaves'] = 512        # num_leaf
params['min_data'] = 500         # min_data_in_leaf
params['min_hessian'] = 0.05     # min_sum_hessian_in_leaf




watchlist = [lgb_valid]
clf = lgb.train(params, lgb_train, 500, watchlist)

#lgb.save_model('zillow_model.txt')

print("Prepare for the prediction ...")

test_data = pd.read_csv("sample_submission.csv")
test_data['parcelid'] = test_data['ParcelId']
test_data = test_data.merge(train_values,  how='inner',
                               on='parcelid')

gc.collect()

clf.reset_parameter({"num_threads":1})

gc.collect()

object_cols = test_data.dtypes[test_data.dtypes==object].index.values

for o in object_cols:
    test_data[o] = (test_data[o]==True)

print("Start prediction ...")
del test_data['ParcelId']
del test_data['201610']
del test_data['201611']
del test_data['201612']
del test_data['201710']
del test_data['201711']
del test_data['201712']

#test_data = test_data.values.astype(np.float32, copy=False)

p_test = clf.predict(test_data, num_iteration=clf.best_iteration)


#p_test = clf.predict(test_data)

sub = pd.read_csv('sample_submission.csv')
for c in sub.columns[sub.columns != 'ParcelId']:
    sub[c] = p_test

sub.to_csv('lgb_starter_1.csv', index=False, float_format='%.4f')