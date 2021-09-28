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
        "dhist_for_rand4_data.csv",
        index_col=0,
        parse_dates=True
)

real_data = df1.iloc[:, 0:51]
rand_data = df2.iloc[:, 0:51]

real_data_sum_o=real_data.sum()
rand_data_sum_o=rand_data.sum()
"""
#rand detected as rand
tp=rand_data_sum_o
#real detected as rand
fp=real_data_sum_o
#real detected as real
tn=561*1200-real_data_sum_o
#rand detected as real
fn=561*1200-rand_data_sum_o
"""
#rand detected as rand
tn=rand_data_sum_o
#real detected as rand
fn=real_data_sum_o
#real detected as real
tp=561*1200-real_data_sum_o
#rand detected as real
fp=561*1200-rand_data_sum_o

pre=tp/(tp+fp)
rec=tp/(tp+fn)

print(rec)
