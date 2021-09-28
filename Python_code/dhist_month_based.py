#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:21:14 2020

@author: andy
"""

import pandas as pd
import glob
import csv

Monthlist=["January","February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#month="December"
#path = r'/home/andy/master_thesis/all_martin/csv_final' # use your path
count=0

df1 = pd.read_csv(
        "lof_for_real_data.csv",
        index_col=0,
        parse_dates=True
)

df2 = pd.read_csv(
        "lof_for_rand4_data.csv",
        index_col=0,
        parse_dates=True
)

app=[]
for month in Monthlist:
   
    c=0
    for row in df1.index: 
        if month in row:
            if c==0:
                rl=df1.loc[row , : ]
                rd=df2.loc[row , : ]
                c=c+1
            else:
                rl=rl+df1.loc[row , : ]
                rd=rd+df2.loc[row , : ]
            
    
    
    
    #real_data = df1.iloc[:, 0:51]
    #rand_data = df2.iloc[:, 0:51]
    
    
    real_data_sum_o=rl
    #print(real_data_sum_o)
    rand_data_sum_o=rd
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
    tn=561*100-real_data_sum_o
    #rand detected as real
    fn=561*100-rand_data_sum_o
    
    
    pre=tp/(tp+fp)
    rec=tp/(tp+fn)
    
    if count==0:
        
        pre.to_csv (r'precision.csv', index = True, header=True)
        rec.to_csv ('precision.csv', mode='a', index=True)
        count=count+1
    else:
        pre.to_csv ('precision.csv', mode='a', index=True)
        rec.to_csv ('precision.csv', mode='a', index=True)

    
    
"""
    if count==0:
        
        rec.to_csv ('precision.csv', mode='a', index=True,columnssequence)
    else:
        pre.to_csv ('precision.csv', mode='a', index=True)
        rec.to_csv ('precision.csv', mode='a', index=True)
"""  
    
