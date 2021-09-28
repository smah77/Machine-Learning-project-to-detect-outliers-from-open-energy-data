#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:36:39 2020

@author: andy
"""

import pandas as pd
import glob
import csv

#path = r'/home/andy/master_thesis/all_martin/csv_final' # use your path

df = pd.read_csv(
        "dhist_for_real_data.csv",
        #index_col=0,
        parse_dates=True
)


