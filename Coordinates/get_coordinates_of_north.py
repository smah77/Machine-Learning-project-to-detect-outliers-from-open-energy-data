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
import numpy as np
from scipy.spatial import distance
#path for server 
#/home/shossain/ms_thesis

df = pd.read_csv(
        "List_of_float_coordinates.csv",
        index_col=0,
        parse_dates=True
)

co=[tuple(values) for values in df.iloc[:,:].values]

nor=(9.2954165,51.1633335,)
#print(nor)
d=[]
with open("sorted_coord.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["long", "lat", "dist"])
    for c in co:
        dist=distance.euclidean(c, nor)
        d=list(c)
        d.append(dist)
        writer.writerow((d[0],) + (d[1],)+(d[2],))
    
    

