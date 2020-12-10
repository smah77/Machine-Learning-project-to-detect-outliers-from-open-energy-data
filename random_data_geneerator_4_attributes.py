#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 20:08:44 2020

@author: andy
"""

import pandas as pd
import glob
import csv
import re
from sklearn.neighbors import LocalOutlierFactor
import math as mt
import numpy as np


path = r'/home/andy/master_thesis/all_martin' # use your path
#print(path)
all_files = glob.glob(path+"/*.csv")
test_len=561
li = []
columns=4
count=0
#print(len(glob.glob('*'))-2)


loop=0
    

num_row1=0


for filename in all_files:
    with_path = filename
    only_file_name = with_path.replace(path+'/', '')
        
    
    df = pd.read_csv(
            only_file_name,
            index_col=0,
            parse_dates=True
    )
    
        
    mn=[]
    mx=[]
    tst=[]
    for c in range(columns):
        mn.append(min(list([tuple(values) for values in df.iloc[:, c:c+1].values])))
        mx.append(max(list([tuple(values) for values in df.iloc[:, c:c+1].values])))
        
    t0=np.random.uniform(mn[0],mx[0], size=(test_len))
    t1=np.random.uniform(mn[1],mx[1], size=(test_len))
    t2=np.random.uniform(mn[2],mx[2], size=(test_len))
    t3=np.random.uniform(mn[3],mx[3], size=(test_len))
    test_data = list(zip(t0,t1,t2,t3))  
        
        #print(rows)
    with open("rand/random {}".format(only_file_name), "w") as f:

        writer = csv.writer(f)
        writer.writerow(["ASWDIFD_S", "ASWDIR_S", "ASWDIRN_S", "Temp_10_m"])
        writer = csv.writer(f)
        for row in test_data:
            writer.writerow(row)
    
