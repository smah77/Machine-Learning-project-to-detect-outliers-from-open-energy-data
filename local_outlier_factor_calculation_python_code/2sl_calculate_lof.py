#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 23:41:06 2020

@author: andy
"""
import csv

import pandas as pd

import numpy as np

import random
import math as mt
from sklearn.neighbors import LocalOutlierFactor
from sklearn import preprocessing

df = pd.read_csv(
  "rat.9.690389633178711-53.39692306518555.csv",
  index_col=0,
  parse_dates=True
)
columns = 4
train_len=mt.floor(len(df)/3*2)
"""
train_data = [tuple(values) for values in df.iloc[:100, 0:columns].values]

test_data=[tuple(values) for values in df.iloc[1:10, 0:columns].values]

"""
train_data = [tuple(values) for values in df.iloc[:train_len, 0:columns].values]

test_data=[tuple(values) for values in df.iloc[train_len:, 0:columns].values]



min_max_scaler = preprocessing.MinMaxScaler()
X_train_minmax = min_max_scaler.fit_transform(train_data)
X_test_minmax=min_max_scaler.fit_transform(test_data)



clf = LocalOutlierFactor(n_neighbors=15, novelty=True,contamination=0.05) 
y_pred_X = clf.fit(X_train_minmax)
y_pred = clf.predict(X_test_minmax)
y_score=clf.score_samples(X_train_minmax)
y_score=list(y_score)
#X_test_minmax=list(X_test_minmax)
#y_neg=clf.negative_outlier_factor_(test_data)

#print(type(y_score))

y_list=y_score

count=0
#print(type(y_list))
for td in range(len(y_list)):
    value = y_list[td]
    print(value)
    if value<-1.5:
        th=1
    else:
        th=0
    count=count+th
    
print(count)
"""
count_outlier=0
for i in range(len(test_data)):
    if test_data[i][4]==1:
        count_outlier=count_outlier+1
        
detected_normal=(len(test_data)-count_outlier)
print("Number of total data: "+str(len(test_data)))
print("Detected as outlier: "+str(count_outlier))
print("Detected as normal: "+str(detected_normal))
"""
with open("out_sl_calculate_lof.csv", "w") as f5:
    writer = csv.writer(f5)
    writer.writerow(["Col 0","1","2","3"])
    for s in range(len(X_train_minmax)):
        writer.writerow((round(X_train_minmax[s][0],4),)+(round(X_train_minmax[s][1],4),)
        +(round(X_train_minmax[s][2],4),)+(round(X_train_minmax[s][3],4),)+(round(y_list[s],4),))


