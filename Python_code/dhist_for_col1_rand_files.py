#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 22:05:51 2020

@author: andy
"""

import math
from itertools import repeat
import numpy as np
from pandas import DataFrame
from code_final.histogram import HBOS
import pandas as pd
import csv
import math as mt
import glob


path = r'/home/andy/master_thesis/all_martin' # use your path
path_rand= r'/home/andy/master_thesis/all_martin/rand'
#print(path)
all_files = glob.glob(path+"/*.csv")

li = []

count=0
#print(len(glob.glob('*'))-2)
loop=0

def histogram(histogram_list, column, data):
    first_index = 0
    result_list = []
    bin_size=bin_size_fl
    # hbos = HBOS()
    while first_index < len(data):
        ret = HBOS.create_dynamic_histogram(histogram_list, data, first_index, bin_size, column, False)
        result_list.append(ret)
        first_index = ret
outlier_col=[]
def dyn_hist(test_data,th_f): 
    count_outlier=0      
    for i in range(len(test_data)):
        total=0
        for c in range(columns):
            #print(test_data[i][c])
            score=0
            for k in range(len(all_hist[c])):
                if test_data[i][c]>=all_hist[c][k][0] and test_data[i][c]<all_hist[c][k][1] :
                    score=all_hist[c][k][3]
            total=score+total
        avg_score=total/4
        th=0
        if avg_score >=th_f:
                th=0
        else:
                th=1
        count_outlier=count_outlier+th

    return count_outlier

def threshold_loop(test_data,th_f,th_t,th_i,only_file_name):
    Test_result1=[] 
    thr=th_f
    Test_result1.append(only_file_name)
    while thr <th_t:
        tl=dyn_hist(test_data,thr)
        
        Test_result1.append(tl)
        
        thr=thr+th_i
    
    return Test_result1
    
    
with open("month_lof/dhist_for_rand_col1_data.csv", "w") as f05:
    writer=csv.writer(f05, delimiter=',',)
    #writer.writerow([''] + range(10))
    row=["Coordinate(Real data detected as outlier)"]
    p=.39
    for i in range(51):
        p=p+.01
        row.append(round(p,2))
    #print(row)
    writer.writerow(row)
         

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
        
        data = DataFrame(data=train_data)
        data = data.apply(sorted)
    
        histogram_list = [[] for _ in range(columns)]
    
        sq_rt_td=mt.sqrt(len(train_data))
        bin_size_fl=mt.floor(sq_rt_td)
        
        #make histogram for each column      
        for c in range(columns):
            histogram(histogram_list, c, data)
        
        
        hlistq=[]
        diff_log=[]
        all_hist=[]
        min_diff_list=[]
        max_diff_list=[]
        for c in range(columns):
            histo_new=histogram_list[c]
            hq=[]
            diff34=[]
            #diff34=[]
            inst=[]
            for i in range(len(histo_new)):
                q=histo_new[i].quantity
                hq.append(q)
                ttt=histo_new[i].range_to-histo_new[i].range_from
                diff34.append(ttt)
                inst.append([histo_new[i].range_from, histo_new[i].range_to, ttt])
            min_diff_list.append(min(diff34))
            max_diff_list.append(max(diff34))
            hlistq.append(hq)
            diff_log.append(diff34)
            all_hist.append(inst)
    
        #normalization of histograms
        for c in range(columns):
            g=0
            for i in range(len(all_hist[c])):
                dist=all_hist[c][i][2]
                g=((max_diff_list[c]-dist)/(max_diff_list[c]-min_diff_list[c]))* 1 +.0
                all_hist[c][i].append(g)
        
        
        #print(only_file_name)
        #print(rand_file)
        
        df2 = pd.read_csv(
                rand_file,
                #index_col=0,
                parse_dates=True
        )
        
        test_data1=[values for values in df2.iloc[:, 0:1].values]
    
        test_data2=[values for values in df.iloc[train_len:, 1:columns].values]
    
        ll1=[]
        for sub in test_data1:
            for item in sub:
                ll1.append(item)
        #print(ll1)
        
        ll2=[]
        ll3=[]
        ll4=[]
        for i in range(len(test_data1)):
            ll2.append(test_data2[i][0])
            ll3.append(test_data2[i][1])
            ll4.append(test_data2[i][2])
            
            
                       
        test_data=list(zip(ll1,ll2,ll3,ll4))
        
        #test_data=[tuple(values) for values in df.iloc[train_len:, 0:columns].values]
        #threshold_loop(test_data,1,1.5,.01,only_file_name)
        get_thr_outlier=threshold_loop(test_data,.4,.91,.01,only_file_name)
        writer.writerow(get_thr_outlier)
        #print(get_thr_outlier)
        #num_outlier=dyn_hist(test_data,.5) 
        #print(filename)
        
        #print(all_hist)
        
        #loop=loop+1
        #if loop==10:
            #break
    


  
    
        
  

