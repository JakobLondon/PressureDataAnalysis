# -*- coding: utf-8 -*-


# import necessary libraries
import pandas as pd
import os
import glob
import csv
import os


# use glob to get all the csv files
# in the folder
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.csv"))

d = {'match_id': [], 'year': [], 'slam': [], 'match_number': [], 'player1': [], 'player2': []}

dfExit = pd.DataFrame(data=d, index=None)

for f in csv_files:

    df = pd.read_csv(f, index_col=0)
    player1read = df[df['player1'].isin(["Roger Federer", "Rafael Nadal", "Novak Djokovic"])]
    #listed = player1read.index.tolist()
    dfExit = pd.concat([dfExit,player1read])

    player2read = df[df['player2'].isin(["Roger Federer", "Rafael Nadal", "Novak Djokovic"])]
    #listed = player1read.index.tolist()
    dfExit = pd.concat([dfExit,player2read])


dfExit.to_csv('C:\\Users\\Jakob\\Downloads\\TempTenisForPogram\\theMatchesTennis.csv')