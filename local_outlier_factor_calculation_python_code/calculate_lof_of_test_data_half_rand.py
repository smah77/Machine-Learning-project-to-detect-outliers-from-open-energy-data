#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 23:39:25 2020

@author: andy
"""

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


df = pd.read_csv(
  "rat.9.690389633178711-53.39692306518555.csv",
  index_col=0,
  parse_dates=True
)
train_data = [tuple(values) for values in df.iloc[:1122, 0:4].values]

df2 = pd.read_csv(
  "output_half_rand.csv",
  
  parse_dates=True
)

test_data = [tuple(values) for values in df2.iloc[:, 0:4].values]

#print(test_data)

#test_data=[tuple(values) for values in df.iloc[1122:, 0:4].values]



from main_lof_class_file import main_lof_class
lof_object = main_lof_class(train_data)
th=0
#print(train_data)
with open("output_half_rand_result.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["ASWDIFD_S", "ASWDIR_S", "ASWDIRN_S", "Temp_10_m", "Value","Outlier"])
    for td in test_data:
        value = lof_object.method_lof(12, td)
        if value>1.3:
            th=1
        else:
            th=0
        writer.writerow(td + (value,)+(th,))
        


