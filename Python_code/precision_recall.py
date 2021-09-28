#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:36:39 2020

@author: andy
"""

import pandas as pd
import glob
import csv

#path = r'/home/andy/master_thesis/all_martin/csv_final' # use your path

df1 = pd.read_csv(
        "dhist_for_real_data.csv",
        index_col=0,
        parse_dates=True
)

df2 = pd.read_csv(
        "dhist_for_rand_col3_data.csv",
        index_col=0,
        parse_dates=True
)

threshold=df1.iloc[:0, 0:51]
#print(threshold)
real_data = df1.iloc[:, 0:51]
rand_data = df2.iloc[:, 0:51]

real_data_sum_o=real_data.sum()
rand_data_sum_o=rand_data.sum()
"""
TP= rand data classified as outlier
FP= real data classified as outlier
TN= real data classified as real
FN= rand data classified as real

Precision(DH)=TP/(TP+FP)=493742/(493742+160023)=.755
Recall(DH)=TP/(TP+FN)=493742/(493742+179458)=.733

"""
#rand detected as rand
tp=rand_data_sum_o
#real detected as rand
fp=real_data_sum_o
#real detected as real
tn=561*1200-real_data_sum_o
#rand detected as real
fn=561*1200-rand_data_sum_o


pre=tp/(tp+fp)
rec=tp/(tp+fn)

print(pre)
#tp.to_csv (r'tp.csv', index = True, header=True)
#fp.to_csv (r'fp.csv', index = True, header=True)
#tn.to_csv (r'tn.csv', index = True, header=True)
#fn.to_csv (r'fn.csv', index = True, header=True)
#threshold.to_csv (r'th.csv', index = False, header=True)
#pre.to_csv (r'precision.csv', index = True, header=True)
#rec.to_csv (r'rec.csv', index = True, header=True)
#print(pre,rec)
