# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 20:47:09 2022

@author: Jakob
"""
import pandas as pd
import numpy as np
import scipy.stats as stats

from csv import reader
import pickle
import tarfile
# open a .spydata file
filename = 'AllData.spydata'
tar = tarfile.open(filename, "r")
# extract all pickled files to the current working directory
tar.extractall()
extracted_files = tar.getnames()
for f in extracted_files:
    if f.endswith('.pickle'):
         with open(f, 'rb') as fdesc:
             data = pickle.loads(fdesc.read())
# or use the spyder function directly:
from spyder_kernels.utils.iofuncs import load_dictionary


data_dict = load_dictionary(filename)
Dictionary = data['Dictionary']
Top3_names = ['R. Federer', 'Roger Federer', 'R. Nadal', 'Rafael Nadal', 'N. Djokovic', 'Novak Djokovic']
Top3_total_df = []
Field_total_df = []
Top3_pressure_df = []
Field_pressure_df = []

Federer_total_df = []
Federer_pressure_df = []
Nadal_total_df = []
Nadal_pressure_df = []
Djokovic_total_df = []
Djokovic_pressure_df = []

for key in Dictionary:
    Match_info = Dictionary[key]
    Match_pressure = Match_info[3]
    for index,row in Match_pressure.iterrows():
        if row['tb1'] == True:
            print(key + " DID IT THEY DID IT")
        if row['tb2'] == True:
            print(key + " DID IT THEY DID IT")

print("END ---------------")
for key in Dictionary:
    All_temp = 0
    Pressure_temp = 0
    Match_info = Dictionary[key]
    Match_ids = Match_info[0]
    Match_side = Match_info[1]
    Match_totals = Match_info[2]
    Match_pressure = Match_info[3]
    for i in range(0,len(Match_ids)):
        match_id = Match_ids[i]
        side = Match_side[i]
        DataFrame_total_row = Match_totals.loc[Match_totals['match_id'] == match_id]
        for index,row in DataFrame_total_row.iterrows():
            if side == 'player1':
                All_temp = All_temp + row['P1DoubleFault']
            else:
                All_temp = All_temp + row['P2DoubleFault']            
        DataFrame_pressure_row = Match_pressure.loc[Match_pressure['match_id'] == match_id]
        # gw = GameWinner
        # sw = SetWinner
        # tb = Tennis Break Point
        # 2: Player 2
        for index,row in DataFrame_pressure_row.iterrows():
            if side == 'player1':
                #Pressure_temp = Pressure_temp + row['gw']
                #Pressure_temp = Pressure_temp + row['sw']
                Pressure_temp = Pressure_temp + row['tb1']
            else:
                #Pressure_temp = Pressure_temp + row['gw2']
                #Pressure_temp = Pressure_temp + row['sw2']
                Pressure_temp = Pressure_temp + row['tb2']
    if key == 'R. Federer' or key == 'Roger Federer':
        Federer_total_df.append(All_temp)
        Federer_pressure_df.append(Pressure_temp)
        
    if key == 'R. Nadal' or key == 'Rafael Nadal':
        Nadal_total_df.append(All_temp)
        Nadal_pressure_df.append(Pressure_temp)
        
    if key == 'N. Djokovic' or key == 'Novak Djokovic':
        Djokovic_total_df.append(All_temp)
        Djokovic_pressure_df.append(Pressure_temp)
        
    
    if key in Top3_names:
        Top3_total_df.append(All_temp)
        Top3_pressure_df.append(Pressure_temp)
    else:
        Field_total_df.append(All_temp)
        Field_pressure_df.append(Pressure_temp)


avgFed = sum(Federer_pressure_df)/sum(Federer_total_df)
print(avgFed)
avgNad = sum(Nadal_pressure_df)/sum(Nadal_total_df)
print(avgNad)
avgDjo = sum(Djokovic_pressure_df)/sum(Djokovic_total_df)
print(avgDjo)

#if len(Federer_total_df) != 0:
    #Federer_df_avgs = sum()

Top3_df_avgs = []            
# for i in range(0,len(Top3_total_df)):
#     if Top3_total_df[i] != 0:
#         Top3_df_avgs.append(Top3_pressure_df[i]/Top3_total_df[i])
    

Field_df_avgs = []
for i in range(0,len(Field_pressure_df)):
    if Field_total_df[i] != 0:
        Field_df_avgs.append(Field_pressure_df[i]/Field_total_df[i])
    
#for avg in Top3_df_avgs:
    #Top3_usable_avg_df = sum(Top3_df_avgs) / len(Top3_df_avgs)
 
    
Top3_usable_avg_df = (avgFed+avgNad+avgDjo)/3

print("This is what you are looking for")
Pressure_test = stats.ttest_1samp(a=Field_df_avgs, popmean=Top3_usable_avg_df)
print(Pressure_test)




Table = data['Table']
for key in Dictionary:
    Match_info = Dictionary[key]
    BP_total = 0
    BP_won = 0
    Team_temp = []
    Match_ids = Match_info[0]
    Match_side = Match_info[1]
    for index,row in Table.iterrows():
        if row['match_id'] in Match_ids:
            index = Match_ids.index(row['match_id'])
            side = Match_side[index]
            if side == 'player1':
                BP_total = BP_total + row['P1BreakPoint']
                BP_won = BP_won + row['P1BreakPointWon']
            else:
                BP_total = BP_total + row['P2BreakPoint']
                BP_won = BP_won + row['P2BreakPointWon']
            if BP_total != 0:
                Avg = 1-(BP_won/BP_total)
                Team_temp.append(Avg)
            else:
                Team_temp.append(None)
    Match_info.append(Team_temp)
    Dictionary[key] = Match_info
    print(key + " is Done!")
    
Top3_bp_list = []
Field_bp_list = []
for key in Dictionary:
    Match_info = Dictionary[key]
    Break_list = Match_info[4]
    if len(list(filter(None,Break_list))) != 0:
        Avg = sum(list(filter(None,Break_list))) / len(list(filter(None,Break_list)))
        if key in Top3_names:
            Top3_bp_list.append(Avg)
        else:
            Field_bp_list.append(Avg)
        
Top3_bp_avg = sum(Top3_bp_list)/len(Top3_bp_list)
print("HEREHEREHERE!")
t_test = stats.ttest_1samp(a=Field_bp_list, popmean=Top3_bp_avg)
print(t_test)
Fed1_Dict = Dictionary['R. Federer']
Fed2_Dict = Dictionary['Roger Federer']     
Nad1_Dict = Dictionary['R. Nadal']
Nad2_Dict = Dictionary['Rafael Nadal']    
Djo1_Dict = Dictionary['N. Djokovic']
Djo2_Dict = Dictionary['Novak Djokovic']         

Fed1_list = Fed1_Dict[4]
Fed2_list = Fed2_Dict[4]
Fed_list = Fed1_list + Fed2_list
Fed_list = list(filter(None,Fed_list))

Nad1_list = Nad1_Dict[4]
Nad2_list = Nad2_Dict[4]
Nad_list = Nad1_list + Nad2_list
Nad_list = list(filter(None,Nad_list))

Djo1_list = Djo1_Dict[4]
Djo2_list = Djo2_Dict[4]
Djo_list = Djo1_list + Djo2_list
Djo_list = list(filter(None,Djo_list))

Fed_bp_avg = sum(Fed_list)/len(Fed_list)
Nad_bp_avg = sum(Nad_list)/len(Nad_list)
Djo_bp_avg = sum(Djo_list)/len(Djo_list)

FedvsNad = stats.ttest_ind(Nad_list,Fed_list)
FedvsDjo = stats.ttest_ind(Djo_list,Fed_list)
DjovsNad = stats.ttest_ind(Djo_list,Nad_list)

print("Federer vs Nadal:")
print(FedvsNad)
print("")
print("Federer vs Djokovic:")
print(FedvsDjo)
print("")
print("Djokovic vs Nadal:")
print(DjovsNad)

FedvsField = stats.ttest_ind(Field_bp_list,Fed_list)
print("Fed vs Field")
print(FedvsField)
print("")
NadvsField = stats.ttest_ind(Field_bp_list,Nad_list)
print("Nad vs Field")
print(NadvsField)
print("")
DjovsField = stats.ttest_ind(Djo_list,Field_bp_list)
print("Djo vs Field")
print(DjovsField)
print("")