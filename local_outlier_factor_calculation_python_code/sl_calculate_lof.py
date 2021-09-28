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


clf = LocalOutlierFactor(n_neighbors=15, novelty=True,contamination=0.00001) 
y_pred_X = clf.fit(train_data)
y_pred = clf.predict(test_data)
y_score=clf.score_samples(test_data)




#print(type(y_list))
for td in range(len(test_data)):
    value = y_list[td]
    #print(value)
    if value<1:
        th=1
    else:
        th=0
    t=list(test_data[td])
    t.append(th)
    test_data[td]=t



count_outlier=0
for i in range(len(test_data)):
    if test_data[i][4]==1:
        count_outlier=count_outlier+1
        
detected_normal=(len(test_data)-count_outlier)
print("Number of total data: "+str(len(test_data)))
print("Detected as outlier: "+str(count_outlier))
print("Detected as normal: "+str(detected_normal))


