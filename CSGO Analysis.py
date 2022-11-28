# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 14:17:48 2022

@author: Jakob
"""
#TTest info
# Get number of rows and mean value from those rows
# Make dataframe of pressure moments vs non pressure moments
# Group into top 3 vs Field
# Averaging the data on a per match basis

import pandas as pd
import os
import glob
import csv
import warnings
warnings.simplefilter("ignore")

Teamfiles = []

root_dir = 'C:\\Users\\Jakob\\Downloads\\CSGO Tournament Stuff'
#for folder, subfolders, files in os.walk(root_dir):
    #for file in files:
        #Teamfiles.append(os.path.join(folder, file))
            


#Teams = [['Titan'],['Team LDLC.com','Team LDLC'],['Ninjas in Pyjamas','Ninjas In Pyjamas'],['Natus Vincere','NaVi'],['Team Dignitas','dignitas'],['iBUYPOWER'],['Virtus.Pro','Virtus.pro'],['mousesports.de','mousesports'],['myXMG'],['Team EnVyUs','EnVyUs'],['HellRaisers'],['Luminosity Gaming'],['PENTA Sports'],['Cloud9.G2A'],['TSM.Kinguin'],['Gambit Gaming'],['Team Liquid'],['G2 Esports','G2 eSports'],['Astralis'],['OpTic Gaming','OpTic.Gaming'],['AGO']]
TeamDict = {
    'Fnatic': ['Fnatic','fnatic'],
    'Astralis': ['Astralis'],
    'NaVi': ['Natus Vincere','NaVi',"""Na'Vi"""],
    "ENCE": ['ENCE'],
    "RNG": ["Renegades"],
    'NRG': ['NRG','NRG Esports'],
    "AVG": ["Avangar"],
    "Vitality": ['Vitality'],
    "Abs": ["Absolute_"],
    'Dragons': ['Astana Dragons'],
    'coL': ['compLexity','compLexity Gaming'],
    'VG': ['VeryGames'],
    'CPH': ['Copenhagen Wolves'],
    'RCE': ['Recursive'],
    'LGB': ['LGB eSports'],
    'Universal': ['Universal Soldiers'],
    '3DMAX': ['Team 3DMAX'],
    'SK': ['SK Gaming'],
    'Epsilon': ['Epsilon', 'Epsilon eSports'],
    'LD': ['Lemondogs'],
    'OG': ['Playfubet OverGaming'],
    'NCG': ['NetcodeGuides'],
    'Manajuma': ['Manajuma'],
    'LC': ['London Conspiracy'],
    'TSM': ['Team SoloMid','TSM', 'TSM Kinguin','TSM.Kinguin'],
    'Kinguin': ['Team Kinguin','Kinguin'],
    'kStars': ['Keyd Stars'],
    'CLG': ['Counter Logic Gaming'],
    'GPlay': ['Gplay.bg'],
    'F3': ['FlipSid3','Flipsid3 Tactics'],
    'GOD': ['GODSENT'],
    'TYLOO': ['Tyloo'],
    'IMT': ['Immortals'],
    'FaZe': ['FaZe Clan', 'FaZe'],
    'Heroic': ['Heroic'],
    'DP': ['Dark Passage'],
    'iGame': ['iGame.com'],
    'SS': ['Space Soldiers'],
    'North': ['North'],
    'MSF': ['Misfits'],
    'BIG': ['BIG'],
    'oNe': ['Team One'],
    'MVPPK': ['MVP PK'],
    'RUS': ['Team Russia'],
    'QBF': ['Quantum Bellator Fire'],
    'MIBR': ['MIBR'],
    'Windigo': ['Windigo Gaming'],
    'Valiance': ['Valiance'],
    'EG': ['Evil Geniuses'],
    "Titan": ['Titan'],
    "LDLC": ['Team LDLC.com','Team LDLC','Team-LDLC.com','Team-LDLC'],
    "NiP": ['Ninjas in Pyjamas','Ninjas In Pyjamas', 'NIP Gaming'],
    'DIG': ['Team Dignitas','dignitas'],
    'iBP': ['iBUYPOWER','Team iBUYPOWER'],
    'VP': ['Virtus.Pro','Virtus.pro','VirtusPro', 'Virtus Pro'],
    'Mouz': ['mousesports.de','mousesports'],
    'Envy': ['Team EnVyUs','EnVyUs','TEAM ENVYUS','Team EnVyUS','ENVYUS','EnVyUS'],
    'HR': ['HellRaisers'],
    'LG': ['Luminosity Gaming','Luminosity'],
    'PENTA': ['PENTA Sports'],
    'C9': ['Cloud9.G2A','Cloud9','Cloud9.G2A','Cloud9 G2A'],
    'Gambit': ['Gambit Gaming','Gambit'],
    'Liquid': ['Team Liquid'],
    'G2': ['G2 Esports','G2 eSports','G2','G2.Esports'],
    'OpTic': ['OpTic Gaming','OpTic.Gaming'],
    'AGO': ['AGO','AGO.Mr.Cat']
}

keynum = 1
for key in TeamDict:
    team = TeamDict[key]
    TeamKillData = pd.DataFrame({'Round': [],'Time death (s)': [],'Killer': [],'Killer SteamID': [],'Killer side': [],'Killer team': [],'Killer bot': [],'Killer blinded': [],'Killer vel X': [],'Killer vel Y': [],'Killer vel Z': [],'Victim': [],'Victim SteamId': [],'Victim side': [],'Victim team': [],'Victim bot': [],'Victim blinded': [],'Assister': [],'Assister SteamID': [],'assister bot': [],'Weapon': [],'Headshot': [],'Crouching': [],'Trade kill': [],'Killer X': [],'Killer Y': [],'Victim X': [],'Victim Y': []})
    TeamFailData = pd.DataFrame({'Round': [],'Time death (s)': [],'Killer': [],'Killer SteamID': [],'Killer side': [],'Killer team': [],'Killer bot': [],'Killer blinded': [],'Killer vel X': [],'Killer vel Y': [],'Killer vel Z': [],'Victim': [],'Victim SteamId': [],'Victim side': [],'Victim team': [],'Victim bot': [],'Victim blinded': [],'Assister': [],'Assister SteamID': [],'assister bot': [],'Weapon': [],'Headshot': [],'Crouching': [],'Trade kill': [],'Killer X': [],'Killer Y': [],'Victim X': [],'Victim Y': []})
    TeamDataData = pd.DataFrame({'Round': [],'Time death (s)': [],'Killer': [],'Killer SteamID': [],'Killer side': [],'Killer team': [],'Killer bot': [],'Killer blinded': [],'Killer vel X': [],'Killer vel Y': [],'Killer vel Z': [],'Victim': [],'Victim SteamId': [],'Victim side': [],'Victim team': [],'Victim bot': [],'Victim blinded': [],'Assister': [],'Assister SteamID': [],'assister bot': [],'Weapon': [],'Headshot': [],'Crouching': [],'Trade kill': [],'Killer X': [],'Killer Y': [],'Victim X': [],'Victim Y': []})
    PressureAll = pd.DataFrame({'Round': [],'Time death (s)': [],'Killer': [],'Killer SteamID': [],'Killer side': [],'Killer team': [],'Killer bot': [],'Killer blinded': [],'Killer vel X': [],'Killer vel Y': [],'Killer vel Z': [],'Victim': [],'Victim SteamId': [],'Victim side': [],'Victim team': [],'Victim bot': [],'Victim blinded': [],'Assister': [],'Assister SteamID': [],'assister bot': [],'Weapon': [],'Headshot': [],'Crouching': [],'Trade kill': [],'Killer X': [],'Killer Y': [],'Victim X': [],'Victim Y': []})
    PressureOne = pd.DataFrame({'Round': [],'Time death (s)': [],'Killer': [],'Killer SteamID': [],'Killer side': [],'Killer team': [],'Killer bot': [],'Killer blinded': [],'Killer vel X': [],'Killer vel Y': [],'Killer vel Z': [],'Victim': [],'Victim SteamId': [],'Victim side': [],'Victim team': [],'Victim bot': [],'Victim blinded': [],'Assister': [],'Assister SteamID': [],'assister bot': [],'Weapon': [],'Headshot': [],'Crouching': [],'Trade kill': [],'Killer X': [],'Killer Y': [],'Victim X': [],'Victim Y': []})
    PressureScore = pd.DataFrame({'Round': [],'Time death (s)': [],'Killer': [],'Killer SteamID': [],'Killer side': [],'Killer team': [],'Killer bot': [],'Killer blinded': [],'Killer vel X': [],'Killer vel Y': [],'Killer vel Z': [],'Victim': [],'Victim SteamId': [],'Victim side': [],'Victim team': [],'Victim bot': [],'Victim blinded': [],'Assister': [],'Assister SteamID': [],'assister bot': [],'Weapon': [],'Headshot': [],'Crouching': [],'Trade kill': [],'Killer X': [],'Killer Y': [],'Victim X': [],'Victim Y': []})
    TeamGeneralData = pd.DataFrame({'Number':[],'Tick':[],'Duration (s)':[],'Winner Clan Name':[],'Winner':[],'End reason':[],'Type':[],'Side':[],'Team':[],'Kills':[],'1K':[],'2K':[],'3K':[],'4K':[],'5K':[],'Trade kill':[],'Jump kills':[],'ADP':[],'TDH':[],'TDA':[],'Bomb Exploded':[],'Bomb planted':[],'Bomb defused':[],'Start money team 1':[],'Start money team 2':[],'Equipement value team 1':[],'Equipement value team 2':[],'Flashbang':[],'Smoke':[],'HE':[],'Decoy':[],'Molotov':[],'Incendiary': []})
    AllRoundData = pd.DataFrame({'Number':[],'Tick':[],'Duration (s)':[],'Winner Clan Name':[],'Winner':[],'End reason':[],'Type':[],'Side':[],'Team':[],'Kills':[],'1K':[],'2K':[],'3K':[],'4K':[],'5K':[],'Trade kill':[],'Jump kills':[],'ADP':[],'TDH':[],'TDA':[],'Bomb Exploded':[],'Bomb planted':[],'Bomb defused':[],'Start money team 1':[],'Start money team 2':[],'Equipement value team 1':[],'Equipement value team 2':[],'Flashbang':[],'Smoke':[],'HE':[],'Decoy':[],'Molotov':[],'Incendiary': []})
    temp_list = []
    for folder, subfolders, files in os.walk(root_dir):
        for file in files:
            if key in folder:
                Teamfiles.append(os.path.join(folder, file))

    
    for filePath in Teamfiles:
        General = pd.read_excel(filePath, 'General', engine='openpyxl')
        Players = pd.read_excel(filePath, 'Players', engine='openpyxl')
        Rounds = pd.read_excel(filePath, 'Rounds', engine='openpyxl')
        Kills = pd.read_excel(filePath, 'Kills', engine='openpyxl')
        
        column = Kills['Round']
        RoundMax = column.max()
        AllRoundData = pd.concat([AllRoundData,Rounds])
        TeamScore = 0
        OtherScore = 0
        for i in range(0,RoundMax):
            RoundKill = Kills[Kills['Round'] == i]
            RoundGen = Rounds[Rounds['Number'] == i]
            TeamKillDF = RoundKill[RoundKill['Killer team'].isin(team)]
            TeamDeathDF = RoundKill[~RoundKill['Killer team'].isin(team)]
           
            TeamKillData = pd.concat([TeamKillData,TeamKillDF],ignore_index = 1)
            TeamKillData = TeamKillData[~TeamKillData['Killer team'].isin(team)]
            
            TeamFailData = pd.concat([TeamFailData,TeamDeathDF],ignore_index = 1)
            TeamFailData = TeamFailData[~TeamFailData['Killer team'].isin(team)]
            
            TeamDataData = pd.concat([TeamDataData,RoundKill],ignore_index=1)
            TeamAlive = 5
            OtherAlive = 5
            CurrentRound = 1
            for index,row in RoundGen.iterrows():
                if row['Winner Clan Name'] in team:
                    TeamScore = TeamScore + 1
                else:
                    OtherScore = OtherScore + 1
            for index,row in RoundKill.iterrows():
                if TeamAlive == 1:
                    crow = row.to_frame().T
                    temp_list = [RoundGen]
                    crow.insert(0,'General',temp_list)
                    PressureAll = pd.concat([PressureAll,crow])
                    PressureOne = pd.concat([PressureOne,crow])
                elif OtherScore == 15 and TeamScore > 11:
                    crow = row.to_frame().T
                    temp_list = [RoundGen]
                    crow.insert(0,'General',temp_list)
                    PressureAll = pd.concat([PressureAll,crow])
                    PressureScore = pd.concat([PressureScore,crow])
                    
                if row['Killer team'] in team:
                    OtherAlive = OtherAlive - 1
                else:
                    TeamAlive =  TeamAlive - 1
                if CurrentRound != row['Round']:
                    CurrentRound = row['Round']
                    TeamAlive = 5
                    OtherAlive = 5
    TeamDict[key] = []
    TeamDict[key].append(AllRoundData)
    winAll = 0
    loseAll = 0
    for index,row in AllRoundData.iterrows():
        if len(team) == 1:
            if team[0] == row['Winner Clan Name']:
                winAll = winAll + 1
            else:
                loseAll = loseAll + 1
        else:
            if team[0] == row['Winner Clan Name'] or team[1] == row['Winner Clan Name']:
                winAll = winAll + 1
            else:
                loseAll = loseAll + 1
                
            
    overall = winAll + loseAll
    if overall == 0:
        print(key +" did not play!")
    else:
        winratio = winAll/overall
        print(key +" had an overall win ratio of: " + str(winratio))
        if winratio == 0:
            print("Yikes")
    
    Teamfiles = []
    PressureRoundData = pd.DataFrame({'Number':[],'Tick':[],'Duration (s)':[],'Winner Clan Name':[],'Winner':[],'End reason':[],'Type':[],'Side':[],'Team':[],'Kills':[],'1K':[],'2K':[],'3K':[],'4K':[],'5K':[],'Trade kill':[],'Jump kills':[],'ADP':[],'TDH':[],'TDA':[],'Bomb Exploded':[],'Bomb planted':[],'Bomb defused':[],'Start money team 1':[],'Start money team 2':[],'Equipement value team 1':[],'Equipement value team 2':[],'Flashbang':[],'Smoke':[],'HE':[],'Decoy':[],'Molotov':[],'Incendiary': []})
    for index,row in PressureAll.iterrows():
        Gen = row['General']
        PressureRoundData = pd.concat([Gen,PressureRoundData]).drop_duplicates().reset_index(drop=True)
    
    PressureRoundOne = pd.DataFrame({'Number':[],'Tick':[],'Duration (s)':[],'Winner Clan Name':[],'Winner':[],'End reason':[],'Type':[],'Side':[],'Team':[],'Kills':[],'1K':[],'2K':[],'3K':[],'4K':[],'5K':[],'Trade kill':[],'Jump kills':[],'ADP':[],'TDH':[],'TDA':[],'Bomb Exploded':[],'Bomb planted':[],'Bomb defused':[],'Start money team 1':[],'Start money team 2':[],'Equipement value team 1':[],'Equipement value team 2':[],'Flashbang':[],'Smoke':[],'HE':[],'Decoy':[],'Molotov':[],'Incendiary': []})
    for index,row in PressureOne.iterrows():
        Gen = row['General']
        PressureRoundOne = pd.concat([Gen,PressureRoundOne]).drop_duplicates().reset_index(drop=True)
    
    PressureRoundScore = pd.DataFrame({'Number':[],'Tick':[],'Duration (s)':[],'Winner Clan Name':[],'Winner':[],'End reason':[],'Type':[],'Side':[],'Team':[],'Kills':[],'1K':[],'2K':[],'3K':[],'4K':[],'5K':[],'Trade kill':[],'Jump kills':[],'ADP':[],'TDH':[],'TDA':[],'Bomb Exploded':[],'Bomb planted':[],'Bomb defused':[],'Start money team 1':[],'Start money team 2':[],'Equipement value team 1':[],'Equipement value team 2':[],'Flashbang':[],'Smoke':[],'HE':[],'Decoy':[],'Molotov':[],'Incendiary': []})
    for index,row in PressureScore.iterrows():
        Gen = row['General']
        PressureRoundScore = pd.concat([Gen,PressureRoundScore]).drop_duplicates().reset_index(drop=True)
    TeamDict[key].append(PressureRoundData)
    winAll = 0
    loseAll = 0
    for index,row in PressureRoundData.iterrows():
        for index,row in PressureRoundScore.iterrows():
            if any(x in row['Winner Clan Name'] for x in team):
                winAll = winAll + 1
            else:
                loseAll = loseAll + 1
    
    overall = winAll + loseAll
    if overall == 0:
        print(key +" did not play!")
    else:
        winratio = winAll/overall
        print(key +" had an overall pressure win ratio of: " + str(winratio))
    TeamDict[key].append(PressureRoundOne)
    winOne = 0
    loseOne = 0
    for index,row in PressureRoundOne.iterrows():
        for index,row in PressureRoundScore.iterrows():
            if any(x in row['Winner Clan Name'] for x in team):
                winOne = winOne + 1
            else:
                loseOne = loseOne + 1
    
    overallOne = winOne + loseOne
    if overallOne == 0:
        print(key +" did not play!")
    else:
        winratioOne = winOne/overallOne
        print(key +" had an one player left pressure win ratio of: " + str(winratioOne))
   
    TeamDict[key].append(PressureRoundScore)       
    winScore = 0
    loseScore = 0
    for index,row in PressureRoundScore.iterrows():
        if any(x in row['Winner Clan Name'] for x in team):
            winScore = winScore + 1
        else:
            loseScore = loseScore + 1
    
    overallScore = winScore + loseScore
    if overallScore == 0:
        print(key +" did not play!")
    else:
        winratioScore = winScore/overallScore
        print(key +" had an score pressure win ratio of: " + str(winratioScore))
    print("\|/ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \|/")