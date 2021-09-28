#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 23:41:06 2020

@author: andy
"""
import time

start = time.time()
#print("hello")

import csv

import pandas as pd

import numpy as np

import random
import math as mt
from sklearn.neighbors import LocalOutlierFactor

#np.argmax(tpr - fpr)

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

#test_data=[tuple(values) for values in df.iloc[train_len:, 0:columns].values]
"""

df2 = pd.read_csv(
  "output_half_rand.csv",
  #index_col=0,
  parse_dates=True
)


test_data=[tuple(values) for values in df2.iloc[:280, 0:columns].values]

test_data2=[tuple(values) for values in df2.iloc[280:, 0:columns].values]

"""
#print(test_data2)

#clf = LocalOutlierFactor(n_neighbors=6, contamination=0.01) 
clf = LocalOutlierFactor(n_neighbors=15, novelty=True,contamination=0.001) 
y_pred_X = clf.fit(train_data)


def test_lof(test_data,r,thr):
    #y_pred = clf.predict(test_data)
    y_score=clf.score_samples(test_data)
    y_score=list(y_score)
    #yd_score=clf.decision_function(test_data)
    #yd_score=list(yd_score)
    #print("fuck"+str(yd_score))
    #print(type(yd_score))
    for td in range(len(test_data)):
        #value = yd_score[td]
        value = -y_score[td]
        #print(value)
        if value>thr:
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
    #print("Number of total data: "+str(len(test_data)))
    #print("Detected as outlier: "+str(count_outlier))
    #print("Detected as normal: "+str(detected_normal))
    if r==1:
        fp=detected_normal/len(test_data)
        #print("Number of Random total data: "+str(len(test_data)))
        #print("Random data detected as normal: "+ str(detected_normal))
        #print("false negative: " +str(fp))
        return [count_outlier,fp]
    if r==2:
        fn=count_outlier/len(test_data)
        #print("Number of Real total data: "+str(len(test_data)))
        #print("Real data detected as outlier: "+ str(count_outlier))
        #print("false positive: " +str(fn))
        return [count_outlier,fn]
    
    
Test_result1=[] 
Test_result2=[]   
sel_Test_result1=[] 
sel_Test_result2=[] 
thr=1
sel_th=1
sub_error_prev=20.001
while thr <1.5:
    
    df2 = pd.read_csv(
      "output_half_rand.csv",
      #index_col=0,
      parse_dates=True
    )
    
    
    test_data=[tuple(values) for values in df2.iloc[:280, 0:columns].values]
    
    test_data2=[tuple(values) for values in df2.iloc[280:, 0:columns].values]
    
    
  
    #print("For 280 random data: \n")    
    Test_result1=test_lof(test_data,1,thr) 
    #print("\n \nFor 280  real data: \n")
    Test_result2=test_lof(test_data2,2,thr)
    sub_error=abs(Test_result2[1])
    
    if sub_error<sub_error_prev:
      sub_error_prev= sub_error
      sel_th=round(thr,4)
      sel_Test_result1=Test_result1
      sel_Test_result2=Test_result2 

    thr=thr+.01
    
print("Optimal Threshold: "+str(sel_th))
print("\nBoth data set of 280 instances")
print("\nrandom 280 : Detected as outlier : "+ str(sel_Test_result1[0]))
print("\nreal 280 : Detected as outlier : "+str(sel_Test_result2[0]))

end = time.time()
print("pased time:"+str(end - start))

"""
    with open("FRR-FAR.CSV", "a") as f5:
        writer = csv.writer(f5)
        #writer.writerow(["Threshold","FP","FN","FAR","FRR"])
        writer.writerow((thr,)+(Test_result1[0],)+(Test_result2[0],)+(Test_result1[1],)+(Test_result2[1],))   
"""        
    

"""
test_data=[tuple(values) for values in df2.iloc[:, 0:columns].values]

clf = LocalOutlierFactor(n_neighbors=12, novelty=True,contamination=0.00001) 
y_pred_X = clf.fit(train_data)
y_pred = clf.predict(test_data)
#sc=score_samples(test_data)

y_list=list(y_pred)

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

"""
