# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 12:53:34 2022

@author: Jakob
"""

import pandas as pd
import os
import glob
import csv
import warnings
warnings.simplefilter("ignore")

root_dir = 'C:\\Users\\Jakob\\Downloads\\CSGO Tournament Stuff'
TeamfilesKILL = []
for folder, subfolders, files in os.walk(root_dir):
    files = [ fi for fi in files if not fi.endswith(".py") ]
    for file in files:
        TeamfilesKILL.append(os.path.join(folder, file))



for filePath in TeamfilesKILL:
    General = pd.read_excel(filePath, 'General', engine='openpyxl')
    for index,row in General.iterrows():
        if row['Name team 1'] == 'Team 1' or row['Name team 2'] == 'Team 2':
            print(filePath)