import pickle5 as pickle

import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer


raw_data = pd.read_csv("datasets/Employee.csv")

# Data Preprocessing

print("Data Preprocessing...")

raw_data.columns = raw_data.columns.str.lower()

for column in list(raw_data.dtypes[raw_data.dtypes == 'object'].index):
  raw_data[column] = raw_data[column].str.lower().str.replace(" ", "_")

# splitting data into full train and test datasets
full_train_datasets, test_datasets = train_test_split(raw_data, test_size=0.1, random_state=1)

full_train_datasets = full_train_datasets.reset_index(drop=True)
test_datasets = test_datasets.reset_index(drop=True)

full_train_labels = full_train_datasets.leaveornot.values
test_labels = test_datasets.leaveornot.values

del full_train_datasets['leaveornot']
del test_datasets['leaveornot']



full_train_dict = full_train_datasets.to_dict(orient='records')
test_dict = test_datasets.to_dict(orient='records')

dv = DictVectorizer(sparse=False)

full_train_features = dv.fit_transform(full_train_dict)
test_features = dv.transform(test_dict)

features = list(dv.get_feature_names_out())

dfull_train = xgb.DMatrix(full_train_features, label=full_train_labels, feature_names=features)
dtest = xgb.DMatrix(test_features, feature_names=features)

print("Done.")

### train model
print("Training model...")

xgb_params = {
  'eta' : 0.1,
  'max_depth' : 5,
  'min_child_weight' : 1,

  'objective' : 'binary:logistic',
  'nthread' : 8,

  'seed' : 1,
  'verbosity' : 1,
}
model = xgb.train(xgb_params, dfull_train, num_boost_round=180)

print("Done.")

# predict with test data
test_pred_labels = model.predict(dtest)

auc = roc_auc_score(test_labels, test_pred_labels)
print("auc is", auc)

# Saving Model

with open('./model/model.bin', 'wb') as f_out: # 'wb' means write-binary
  pickle.dump((dv, model), f_out)