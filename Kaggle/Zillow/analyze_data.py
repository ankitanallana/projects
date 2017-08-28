import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

print("Reading train_2016.csv")
train_data = pd.read_csv('train_2016.csv')
print("number of records - ", len(train_data))

print("Reading properties_2016.csv")
log_values = pd.read_csv('properties_2016.csv')
print("number of records - ", len(log_values))

print("Merging data")
merged_data = log_values.merge(train_data, how='inner',
                               on='parcelid')

print("Merge complete")
print("Number of records - ", len(merged_data))

cols = list(merged_data.columns)

all_data = merged_data


object_cols = merged_data.dtypes[merged_data.dtypes==object].index.values

for o in object_cols:
    merged_data[o] = (merged_data[o]==True)

train_data, valid_data = train_test_split(merged_data,
                                          test_size=0.1,
                                          random_state=55)

y_values_train = train_data.iloc[:, 58:59]
x_values_train = train_data.iloc[:, 1:58]

y_values_test = valid_data.iloc[:, 58:59]
x_values_test = valid_data.iloc[:, 1:58]

print("training data len - ", len(x_values_train))
print("testing data len - ", len(x_values_test))

d_train = xgb.DMatrix(x_values_train, label=y_values_train)
d_test = xgb.DMatrix(x_values_test, label=y_values_test)

params = {}
params['eta'] = 0.02
params['objective'] = 'reg:linear'
params['eval_metric'] = 'mae'
params['max_depth'] = 4
params['silent'] = 1

watchlist = [(d_train, 'train'), (d_test, 'valid')]
clf = xgb.train(params, d_train, 10000, watchlist, early_stopping_rounds=100, verbose_eval=10)

# Test Set

test_set = pd.read_csv('sample_submission.csv')
test_set['parcelid'] = test_set['ParcelId']
test_set = test_set.merge(train_data, how='inner', on='parcelid')

object_cols = test_set.dtypes[test_set.dtypes==object].index.values

for o in object_cols:
    test_set[o] = (test_set[o]==True)

all_columns = list(test_set.columns)
all_columns.remove("logerror")
all_columns.remove("transactiondate")
all_columns.remove("ParcelId")
all_columns.remove("parcelid")

all_columns.remove("201710")
all_columns.remove("201712")
all_columns.remove("201610")
all_columns.remove("201612")
all_columns.remove("201611")
all_columns.remove("201711")

x_values_test = test_set[all_columns]
d_test = xgb.DMatrix(x_values_test)

p_test = clf.predict(d_test)


