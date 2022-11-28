# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

Dictionary = {}

from csv import reader

# open file in read mode

# Original with open names:
#C:\\Users\\16309\\Desktop\\TennisDataMatches\\PlayerNames.csv
#C:\\Users\\16309\\Desktop\\TennisDataMatches\\11-19-matches.csv
#C:\\Users\\16309\\Downloads\\2015 Slams\\tennis_slam_pointbypoint-master\\2015 combined slams.csv

with open("PlayerNames.csv", 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        Dictionary[row[0]] = []

for key in Dictionary:
    match_id_list = []
    Side = []
    with open("11-19-matches.csv", 'r') as read_obj2:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj2)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            if row[5] == key:
                match_id_list.append(row[1])
                Side.append('player1')
            if row[6] == key:
                match_id_list.append(row[1])
                Side.append('player2')
    Dictionary[key].append(match_id_list)
    Dictionary[key].append(Side)
   # print(Dictionary[key][0])
    #print()
    
# Dictionary = {
#     'Roger Federer': ['Roger Federer', 'R. Federer']}

#---------------------player names have been added to dictionary-----
#---------below creates the data frame (P1)-------------------------------
df = pd.read_csv("2015 combined slams.csv")

Table = pd.DataFrame({"match_id": [],"P1DoubleFault": [],'P1UnfErr': [], 'GameWinner': [], 'SetWinner':[], 'P1BreakPoint': [], 'P1BreakPointWon':[]})


pivot = pd.pivot_table(df, index = ["match_id"], values ='P1DoubleFault',  aggfunc= np.sum)
pivot.reset_index(inplace=True)

pivot2 = pd.pivot_table(df, index = ["match_id"], values ='P1UnfErr',  aggfunc= np.sum)
pivot2.reset_index(inplace=True)

pivot3 = pd.pivot_table(df, index = ["match_id"], values ='GameWinner',  aggfunc= np.sum)
pivot3.reset_index(inplace=True)

pivot4 = pd.pivot_table(df, index = ["match_id"], values ='SetWinner',  aggfunc= np.sum)
pivot4.reset_index(inplace=True)

pivot5 = pd.pivot_table(df, index = ["match_id"], values ='P1BreakPoint',  aggfunc= np.sum)
pivot5.reset_index(inplace=True)

pivot6 = pd.pivot_table(df, index = ["match_id"], values ='P1BreakPointWon',  aggfunc= np.sum)
pivot6.reset_index(inplace=True)

#------(P2 pivots)----------------------------------
pivot7 = pd.pivot_table(df, index = ["match_id"], values ='P2DoubleFault',  aggfunc= np.sum)
pivot7.reset_index(inplace=True)

pivot8 = pd.pivot_table(df, index = ["match_id"], values ='P2UnfErr',  aggfunc= np.sum)
pivot8.reset_index(inplace=True)

pivot9 = pd.pivot_table(df, index = ["match_id"], values ='P2BreakPoint',  aggfunc= np.sum)
pivot9.reset_index(inplace=True)

pivot10 = pd.pivot_table(df, index = ["match_id"], values ='P2BreakPointWon',  aggfunc= np.sum)
pivot10.reset_index(inplace=True)

#----------P1(concats)-----------
Table = pd.concat([pivot, Table],axis=1,copy=True)
Table = pd.concat([pivot2, Table],axis=1,copy=True)
Table = pd.concat([pivot3, Table],axis=1,copy=True)
Table = pd.concat([pivot4, Table],axis=1,copy=True)
Table = pd.concat([pivot5, Table],axis=1,copy=True)
Table = pd.concat([pivot6, Table],axis=1,copy=True)
#----------P2-----------
Table = pd.concat([pivot7, Table],axis=1,copy=True)
Table = pd.concat([pivot8, Table],axis=1,copy=True)
Table = pd.concat([pivot9, Table],axis=1,copy=True)
Table = pd.concat([pivot10, Table],axis=1,copy=True)


Table = Table.loc[:,~Table.columns.duplicated()]

c= list(df.columns)

data_cols = ['P1DoubleFault',
             'P1UnfErr',
             'GameWinner',
             "SetWinner",
             'P1BreakPoint',
             'P1BreakPointWon',
             'P2DoubleFault',
             'P2UnfErr',
             'P2BreakPoint',
             'P2BreakPointWon']

df = df.reindex(columns=data_cols)
#or new_df = df[data_cols]
#print(df.head(100))

#could remove "match_id"------new_df['match_id'].str.replace(r'match_id', '').astype(float)

#print(pivot, pivot2, pivot3, pivot4, pivot5,pivot6)

# if df[df[pivot] and df[df[pivot3]] == 1:
#       x = x+1

#----above created the dataframe needed---------

#------Below should compare rows within the dataframe for player 1-----
Game_winner = 0
df_gw = df['P1DoubleFault'] == df['GameWinner']
for index, row in df.iterrows():
    if row['P1DoubleFault'] == 1 and row['GameWinner'] == 2:
        Game_winner = Game_winner + 1
        
    

Set_winner = 0
df_sw = df['P1DoubleFault'] == df["SetWinner"]
for index, row in df.iterrows():
    if row['P1DoubleFault'] == 1 and row["SetWinner"] == 2:
        Set_winner = Set_winner + 1
    
# Nadaltemp = (Dictionary.get('R. Nadal') and Dictionary.get('Rafael Nadal'));
# Nadal = Nadaltemp[0]

# print(len(Nadal))

Tie_breaks = 0
df_tb = df['P1DoubleFault'] == df['P1BreakPoint']
for index, row in df.iterrows():
    if row['P1DoubleFault'] == 1 and row['P1BreakPoint'] == 1:
        Tie_breaks = Tie_breaks + 1

#------Below should compare rows within the dataframe for player 2-----
Game_winner2 = 0
df_gw2 = df['P2DoubleFault'] == df['GameWinner']
for index, row in df.iterrows():
    if row['P2DoubleFault'] == 1 and row['GameWinner'] == 1:
        Game_winner2 = Game_winner2 + 1
        
Set_winner2 = 0
df_sw2 = df['P2DoubleFault'] == df["SetWinner"]
for index, row in df.iterrows():
    if row['P2DoubleFault'] == 1 and row["SetWinner"] == 1:
        Set_winner2 = Set_winner2 + 1
        
Tie_breaks2 = 0
df_tb = df['P2DoubleFault'] == df['P2BreakPoint']
for index, row in df.iterrows():
    if row['P2DoubleFault'] == 1 and row['P2BreakPoint'] == 1:
        Tie_breaks2 = Tie_breaks2 + 1
#--------Append summed up points to dictionary------------
# for key in Dictionary:
#     lister = []
#     with open("C:\\Users\\16309\\Downloads\\2015 Slams\\tennis_slam_pointbypoint-master\\2015 combined slams.csv", 'r') as read_obj3:
#         # pass the file object to reader() to get the reader object
#         csv_reader = reader(read_obj3)
#         # Iterate over each row in the csv using reader object
#         for row in csv_reader:
#             if row[2] == key:
#                 lister.append(row[1])
#     Dictionary[key].append(lister)

Top3_pressure = []
Top3_non_pressure = []
Field_pressure = []
Field_non_pressure = []
Top3_names = ['R. Federer', 'Roger Federer', 'R. Nadal', 'Rafael Nadal', 'N. Djokovic', 'Novak Djokovic']
for key in Dictionary:
    # True indicates that the key resides within the Top 3 players, False means that the key is in the field
    if key in Top3_names:
        Top3_check = True
    else:
        Top3_check = False
    Match_info = Dictionary[key]
    Match_ids = Match_info[0]
    Player_side = Match_info[1]
    for i in range(0,len(Match_ids)):
        Current_id = Match_ids[i]
        Current_side = Player_side[i]




