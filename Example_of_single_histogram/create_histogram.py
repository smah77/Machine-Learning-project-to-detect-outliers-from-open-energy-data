#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 19:25:08 2020

@author: andy
"""
import math
from itertools import repeat

import numpy as np
from pandas import DataFrame

from histogram import HBOS
import pandas as pd
import csv
import math as mt

df = pd.read_csv(
  "rat.1.4233369827270508-56.71907424926758-1st-April-9am.csv",
  index_col=0,
  parse_dates=True
)
columns = 4
train_len=mt.floor(len(df)/3*2)


train_data = [tuple(values) for values in df.iloc[:train_len, 0:columns].values]

test_data=[tuple(values) for values in df.iloc[1123:1126, 0:columns].values]

#print(test_data)

data = DataFrame(data=train_data)
data = data.apply(sorted)

#data = DataFrame(data=[1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 10])
histogram_list = [[] for _ in range(columns)]

#train_data = [tuple(values) for values in df.iloc[:1122, 0:columns].values]

#test_data=[tuple(values) for values in df.iloc[1122:, 0:columns].values]
sq_rt_td=mt.sqrt(len(train_data))
bin_size_fl=mt.floor(sq_rt_td)
#print(bin_size_fl)

def histogram(histogram_list, column, data):
    first_index = 0
    result_list = []
    bin_size=bin_size_fl
    # hbos = HBOS()
    while first_index < len(data):
        ret = HBOS.create_dynamic_histogram(histogram_list, data, first_index, bin_size, column, False)
        result_list.append(ret)
        first_index = ret
      
for c in range(columns):
    histogram(histogram_list, c, data)
    #print(type(histogram))
 
"""

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



for c in range(columns):
    g=0
    for i in range(len(all_hist[c])):
        dist=all_hist[c][i][2]
        g=((max_diff_list[c]-dist)/(max_diff_list[c]-min_diff_list[c]))* 1 +.0
        all_hist[c][i].append(g)


"""
    
        
    

    
    

    




    
    
    
    
#print(len(total_hist[3]))
    



"""
cinema = []

for j in range(5):
    column = []
    for i in range(5):
        column.append(0)
    cinema.append(column)
"""

#print(result_list)
#print(histogram_list)
#print(len(histogram_list))
#assert result_list == [6, 9, 14, 16, 17, 23, 27, 28]


histogram = histogram_list[0]
result_list_two = []
start=[]
end=[]
diff=[]


for i in range(len(histogram)):
    q=histogram[i].quantity
    ttt=histogram[i].range_to-histogram[i].range_from
    diff.append(ttt)

#print(min(diff))

max_h1=max(diff)
min_h1=min(diff)


with open("histogram1.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["ASWDIFD_S_from","ASWDIFD_S_to","diff","nor"])
    for hst in range(len(histogram)):
        fr=histogram[hst].range_from
        to=histogram[hst].range_to
        diffr=to-fr
        
        g=((max_h1-diffr)/(max_h1-min_h1))* 1 +.0
        writer.writerow((fr,)+(to,)+(diffr,)+(g,))

    
            
            
histogram2 = histogram_list[1]

diff2=[]
t2=0
for i in range(len(histogram2)):
    t2=histogram2[i].range_to-histogram2[i].range_from
    diff2.append(t2)

#print(min(diff))

max_h2=max(diff2)
min_h2=min(diff2)



with open("histogram2.csv", "w") as f2:
    writer = csv.writer(f2)
    writer.writerow(["ASWDIR_S_from","ASWDIR_S_to","diff","nor"])
    for hst in range(len(histogram2)):
        fr2=histogram2[hst].range_from
        to2=histogram2[hst].range_to
        diffr2=to2-fr2
        
        g2=((max_h2-diffr2)/(max_h2-min_h2))* 1+.0
        writer.writerow((fr2,)+(to2,)+(diffr2,)+(g2,))


histogram3 = histogram_list[2]

diff3=[]
t3=0
for i in range(len(histogram3)):
    t3=histogram3[i].range_to-histogram3[i].range_from
    diff3.append(t3)

#print(min(diff))

max_h3=max(diff3)
min_h3=min(diff3)

with open("histogram3.csv", "w") as f3:
    writer = csv.writer(f3)
    writer.writerow(["ASWDIRN_S_from","ASWDIRN_S_to","diff","nor"])
    for hst in range(len(histogram3)):
        fr3=histogram3[hst].range_from
        to3=histogram3[hst].range_to
        diffr3=to3-fr3
        
        g3=((max_h3-diffr3)/(max_h3-min_h3))* 1+.0
        writer.writerow((fr3,)+(to3,)+(diffr3,)+(g3,))
        
        
histogram4 = histogram_list[3]


diff4=[]
t4=0
for i in range(len(histogram4)):
    t4=histogram4[i].range_to-histogram4[i].range_from
    diff4.append(t4)

#print(min(diff))

max_h4=max(diff4)
min_h4=min(diff4)


with open("histogram4.csv", "w") as f4:
    writer = csv.writer(f4)
    writer.writerow(["Temp_10_m_from","Temp_10_m_to","diff","nor"])
    for hst in range(len(histogram4)):
        fr4=histogram4[hst].range_from
        to4=histogram4[hst].range_to
        diffr4=to4-fr4
        
        g4=((max_h4-diffr4)/(max_h4-min_h4))* 1+.0
        writer.writerow((fr4,)+(to4,)+(diffr4,)+(g4,))



