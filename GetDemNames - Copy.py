# -*- coding: utf-8 -*-


# import necessary libraries
import pandas as pd
import os
import glob
  
  
# use glob to get all the csv files 
# in the folder
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.csv"))


for f in csv_files:

    df = pd.read_csv(f,index_col=0)

    player1read = df[df['player1'].isin(["Roger Federer","Rafael Nadal","Novak Djokovic"])]
    listed = player1read.index.tolist()
    for part in listed:
        print(part)
        
    player2read = df[df['player2'].isin(["Roger Federer","Rafael Nadal","Novak Djokovic"])]
    listed = player2read.index.tolist()
    for part in listed:
        print(part)