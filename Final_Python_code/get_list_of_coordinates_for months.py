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
import geopandas as gpd
from shapely.geometry import Polygon
#path for server 
#/home/shossain/ms_thesis
path = r'/home/andy/master_thesis/all_martin' # use your path
print(path)
all_files = glob.glob(path+"/*.csv")

li = []

count=0
print(len(glob.glob('*'))-2)
month="January"

"""
for filename in all_files:
    with_path = filename
    only_file_name = with_path.replace(path+'/', '')
    if month in only_file_name:
    #print (month_file)
        count=count+1
"""
#print(count)



with open("List of float coordinates.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Number", "Coordinate"])
    for filename in all_files:
        with_path = filename
        only_file_name = with_path.replace(path+'/', '')
        if month in only_file_name:
            #print(only_file_name)
            s=only_file_name
            x='rat.'
            start = s.find(x) + len(x)  
            end = s.find('-1st-January-9am.csv', start)
            get_name=s[start:end]
            spilted=get_name.split('-')
            #print(spilted)
            
            #print(get_name)
            count=count+1
            writer.writerow((count,) + (spilted[0],)+ (spilted[1],))
            

#frame = pd.concat(li, axis=0, ignore_index=True