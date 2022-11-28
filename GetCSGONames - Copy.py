# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 23:47:10 2022

@author: Jakob
"""

import pandas as pd
import os
import glob
import csv
import warnings
warnings.simplefilter("ignore")
Teamfiles = []
root_dir = 'C:\\Users\\Jakob\\Downloads\\CSGO Tournament Stuff'

for folder, subfolders, files in os.walk(root_dir):
    for file in files:
        Teamfiles.append(os.path.join(folder, file))

teamlist = []

for filePath in Teamfiles:
    General = pd.read_excel(filePath, 'General', engine='openpyxl')
    
    for index,row in General.iterrows():
        team1 = row['Name team 1']
        team2 = row['Name team 2']
        
        
        teamlist.append(team1)
        teamlist.append(team2)

diction = list(dict.fromkeys(teamlist))
for key in diction:
    print(key)