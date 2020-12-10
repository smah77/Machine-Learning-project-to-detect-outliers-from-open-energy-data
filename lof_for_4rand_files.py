#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 23:20:37 2020

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
path_rand= r'/home/andy/master_thesis/all_martin/rand'
#print(path)
all_files = glob.glob(path+"/*.csv")

li = []

count=0
#print(len(glob.glob('*'))-2)

month="January"
loop=0



def test_lof(test_data,thr):
    y_score=clf.score_samples(test_data)
    y_score=list(y_score)
    result=[]
    for td in range(len(test_data)):
        value = -y_score[td]
        if value>thr:
            th=1
        else:
            th=0
        result.append(th)
        #test_data[td]=t
        #print(test_data)
    
    
    count_outlier=0
    for i in range(len(test_data)):
        if result[i]==1:
            count_outlier=count_outlier+1
            
    return count_outlier
    

def threshold_loop(test_data,th_f,th_t,th_i,only_file_name):         
    Test_result1=[] 
    thr=th_f
    Test_result1.append(only_file_name)
    while thr <th_t:
        tl=test_lof(test_data,thr)
        
        Test_result1.append(tl)
        
        thr=thr+th_i
    
    return Test_result1

num_row1=0
with open("month_lof/lof_for_rand4_data.csv", "w") as f05:
    writer=csv.writer(f05, delimiter=',',)
    #writer.writerow([''] + range(10))
    row=["Coordinate(Real data detected as outlier)"]
    p=1
    for i in range(50):
        p=p+.01
        row.append(round(p,2))
    #print(row)
    writer.writerow(row)
    #writer = csv.writer(f05)
    #writer.writerow(["Number", "Coordinate","Threshold", "False Neg","True Pos"])    


    for filename in all_files:
        with_path = filename
        
        only_file_name = with_path.replace(path+'/', '')
        rand_file=path_rand+"/random "+only_file_name
    
        df = pd.read_csv(
                only_file_name,
                index_col=0,
                parse_dates=True
        )
        
        columns = 4
        train_len=mt.floor(len(df)/3*2)
        test_len=mt.floor(len(df)/3*1)
        train_data = [tuple(values) for values in df.iloc[:train_len, 0:columns].values]
    
        
        
        
        df2 = pd.read_csv(
                rand_file,
                #index_col=0,
                parse_dates=True
        )
        
        test_data=[tuple(values) for values in df2.iloc[:, 0:columns].values]
        
        clf = LocalOutlierFactor(n_neighbors=12, novelty=True,contamination=0.05) 
        y_pred_X = clf.fit(train_data)
        
        
        get_thr_outlier=threshold_loop(test_data,1,1.5,.01,only_file_name)
        #print(get_thr_outlier)
        
        #print(only_file_name)
        
        #writer.writerows([only_file_name])
        writer.writerow(get_thr_outlier)
        #print(get_thr_outlier)
        #loop=loop+1
        #if loop==3:
            #break

        #loop=loop+1
        #if loop==3:
            #break
                
        #print(rand_file_name)
        
