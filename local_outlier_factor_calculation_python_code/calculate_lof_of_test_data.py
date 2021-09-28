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




#one_third=561
"""

"""
"""
#2 X 2 dimensional float array  within 77.5 to 125.5
random_float_array1 = np.random.uniform(0.00, 167.9045, size=(280))
random_float_array2 = np.random.uniform(0.00, 188.723, size=(280))
random_float_array3 = np.random.uniform(0.00, 736.804, size=(280))
random_float_array4 = np.random.uniform(131.229, 142.4545, size=(280))

rows = zip(random_float_array1,random_float_array2,random_float_array3,random_float_array4)
print(rows)


with open("output_tt.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["ASWDIFD_S", "ASWDIR_S", "ASWDIRN_S", "Temp_10_m"])
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
#print(type(train_data))


#print(test_data)
#print(train_data)
"""
"""
one_third=561
one_third_half=280

0	0	0	131.229

167.9045	
188.723	
736.804	
142.4545


"""

    

from main_lof_class_file import main_lof_class
lof_object = main_lof_class(train_data)

th=0

for td in range(len(test_data)):
    value = lof_object.method_lof(12, test_data[td])
    print(value)
    if value>1.25:
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





"""




#print(train_data)
with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["ASWDIFD_S", "ASWDIR_S", "ASWDIRN_S", "Temp_10_m", "Value","Outlier"])
    for td in test_data:
        value = lof_object.method_lof(5, td)
        if value>1.2:
            th=1
        else:
            th=0
        writer.writerow(td + (value,)+(th,))

        
"""

