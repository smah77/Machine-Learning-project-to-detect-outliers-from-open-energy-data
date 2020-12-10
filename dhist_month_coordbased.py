#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:21:14 2020

@author: andy
"""

import pandas as pd
import glob
import csv

northlist=["9.160819053649902-55.50043869018555",
"9.098466873168945-54.2370491027832",
"7.171267032623291-55.47554016113281",
"7.16704797744751-54.2116432189941",
"9.127167701721191-56.69429016113281",
]

#month="December"
#path = r'/home/andy/master_thesis/all_martin/csv_final' # use your path
count=0

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

app=[]
cnt=0
for month in northlist:
   
    c=0
    for row in df1.index: 
        if month in row:
            print(row)
            cnt=cnt+1
            if c==0:
                rl=df1.loc[row , : ]
                rd=df2.loc[row , : ]
                c=c+1
            else:
                rl=rl+df1.loc[row , : ]
                rd=rd+df2.loc[row , : ]
            
    
    
    
    #real_data = df1.iloc[:, 0:51]
    #rand_data = df2.iloc[:, 0:51]
    #print(rl)
    
    real_data_sum_o=rl
    #print(real_data_sum_o)
    rand_data_sum_o=rd
    
    #rand detected as rand
    tp=rand_data_sum_o
    #real detected as rand
    fp=real_data_sum_o
    #real detected as real
    tn=561*12-real_data_sum_o
    #rand detected as real
    fn=561*12-rand_data_sum_o
    
    
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
"""
north last 5:
"7.1910719871521-56.6775512695313",
"9.14186477661133-52.9810943603516",
"7.14700841903687-53.0095405578613",
"11.0422697067261-55.4892196655274",
"11.0311403274536-54.2330360412598"
"""  
