# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 14:17:48 2022

@author: Jakob
"""
#TTest info
# Get number of rows and mean value from those rows
# Make dataframe of pressure moments vs non pressure moments
# Group into top 3 vs Field
# Averaging the data for all time
# Average for each top 3
# Average for each field player, making a list
# For comparing the big 3 against each other, 2 sample
#



import pandas as pd
import os
import glob
import csv
import warnings
import scipy.stats as stats

warnings.simplefilter("ignore")



root_dir ="C:\\Users\\Jakob\\Downloads\\CSGO Tournament Stuff"
#for folder, subfolders, files in os.walk(root_dir):
    #for file in files:
        #Teamfiles.append(os.path.join(folder, file))
            
Howmany = 0

#Teams = [['Titan'],['Team LDLC.com','Team LDLC'],['Ninjas in Pyjamas','Ninjas In Pyjamas'],['Natus Vincere','NaVi'],['Team Dignitas','dignitas'],['iBUYPOWER'],['Virtus.Pro','Virtus.pro'],['mousesports.de','mousesports'],['myXMG'],['Team EnVyUs','EnVyUs'],['HellRaisers'],['Luminosity Gaming'],['PENTA Sports'],['Cloud9.G2A'],['TSM.Kinguin'],['Gambit Gaming'],['Team Liquid'],['G2 Esports','G2 eSports'],['Astralis'],['OpTic Gaming','OpTic.Gaming'],['AGO']]
TeamDict = {
    'Astralis': ['Astralis'],
    'VP': ['Virtus.Pro','Virtus.pro','VirtusPro', 'Virtus Pro'],
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
    'Fnatic': ['Fnatic','fnatic'],
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

# For each map, calculate the pressure rounds vs the nonpressure
# rounds win rate. Then average these into one single win %
# for each top 3. If they are field, leave them seperated
# to be compared in the t-test towards that one top 3 average

Top3Total = []
FieldTotal = []
Top3PresTotal = []
FieldPresTotal = []

VPPresTotal = []
VP_pres_list = []
FnaticPresTotal = []
Fnatic_pres_list = []
Astralis_pres_list = []
AstralisPresTotal = []
NaVi_pres_list = []
NaViPresTotal = []

Fnatic_pres_avg = 0
VP_pres_avg = 0
NaVi_pres_avg = 0
Astralis_pres_avg = 0
Check = 1


keynum = 1
for key in TeamDict:
    Top3pres = []
    Fieldpres = []
    Top3non = []
    Fieldnon = []
    temp_all_percent = []
    temp_pres_percent = []
    Teamfiles = []
    team = TeamDict[key]
    TeamKillData = pd.DataFrame({'Round': [],'Time death (s)': [],'Killer': [],'Killer SteamID': [],'Killer side': [],'Killer team': [],'Killer bot': [],'Killer blinded': [],'Killer vel X': [],'Killer vel Y': [],'Killer vel Z': [],'Victim': [],'Victim SteamId': [],'Victim side': [],'Victim team': [],'Victim bot': [],'Victim blinded': [],'Assister': [],'Assister SteamID': [],'assister bot': [],'Weapon': [],'Headshot': [],'Crouching': [],'Trade kill': [],'Killer X': [],'Killer Y': [],'Victim X': [],'Victim Y': []})
    TeamFailData = pd.DataFrame({'Round': [],'Time death (s)': [],'Killer': [],'Killer SteamID': [],'Killer side': [],'Killer team': [],'Killer bot': [],'Killer blinded': [],'Killer vel X': [],'Killer vel Y': [],'Killer vel Z': [],'Victim': [],'Victim SteamId': [],'Victim side': [],'Victim team': [],'Victim bot': [],'Victim blinded': [],'Assister': [],'Assister SteamID': [],'assister bot': [],'Weapon': [],'Headshot': [],'Crouching': [],'Trade kill': [],'Killer X': [],'Killer Y': [],'Victim X': [],'Victim Y': []})
    TeamDataData = pd.DataFrame({'Round': [],'Time death (s)': [],'Killer': [],'Killer SteamID': [],'Killer side': [],'Killer team': [],'Killer bot': [],'Killer blinded': [],'Killer vel X': [],'Killer vel Y': [],'Killer vel Z': [],'Victim': [],'Victim SteamId': [],'Victim side': [],'Victim team': [],'Victim bot': [],'Victim blinded': [],'Assister': [],'Assister SteamID': [],'assister bot': [],'Weapon': [],'Headshot': [],'Crouching': [],'Trade kill': [],'Killer X': [],'Killer Y': [],'Victim X': [],'Victim Y': []})
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
            PressureAll = pd.DataFrame({'Round': [],'Time death (s)': [],'Killer': [],'Killer SteamID': [],'Killer side': [],'Killer team': [],'Killer bot': [],'Killer blinded': [],'Killer vel X': [],'Killer vel Y': [],'Killer vel Z': [],'Victim': [],'Victim SteamId': [],'Victim side': [],'Victim team': [],'Victim bot': [],'Victim blinded': [],'Assister': [],'Assister SteamID': [],'assister bot': [],'Weapon': [],'Headshot': [],'Crouching': [],'Trade kill': [],'Killer X': [],'Killer Y': [],'Victim X': [],'Victim Y': []})
            All = pd.DataFrame({'Round': [],'Time death (s)': [],'Killer': [],'Killer SteamID': [],'Killer side': [],'Killer team': [],'Killer bot': [],'Killer blinded': [],'Killer vel X': [],'Killer vel Y': [],'Killer vel Z': [],'Victim': [],'Victim SteamId': [],'Victim side': [],'Victim team': [],'Victim bot': [],'Victim blinded': [],'Assister': [],'Assister SteamID': [],'assister bot': [],'Weapon': [],'Headshot': [],'Crouching': [],'Trade kill': [],'Killer X': [],'Killer Y': [],'Victim X': [],'Victim Y': []})
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
                Check = 1
                if TeamAlive == 1:
                    PressureAll = pd.concat([PressureAll,RoundGen])
                    Check = 0
                if OtherScore == 15 and TeamScore > 10:
                    PressureAll = pd.concat([PressureAll,RoundGen])
                    Howmany = Howmany + 1
                    Check = 0
                if Check == 0:
                    break
                if row['Killer team'] in team:
                    OtherAlive = OtherAlive - 1
                else:
                    TeamAlive =  TeamAlive - 1
                if CurrentRound != row['Round']:
                    CurrentRound = row['Round']
                    TeamAlive = 5
                    OtherAlive = 5
            All = pd.concat([All,RoundGen])
            PressureAll = PressureAll.reset_index(drop=True)
            if len(PressureAll.index):
                for index,row in RoundGen.iterrows():
                    if row['Winner Clan Name'] in team:
                        temp_pres_percent.append(1)
                    else:
                        temp_pres_percent.append(0)
            All = All.reset_index(drop=True)
            if len(All.index):
                for index,row in RoundGen.iterrows():
                    if row['Winner Clan Name'] in team:
                        temp_all_percent.append(1)
                    else:
                        temp_all_percent.append(0)
        # win = temp_non_percent.count(1)
        # lose = temp_non_percent.count(0)
        # if win != 0 and lose != 0:
        #     avg = win/(win+lose)
        # else: 
        #     avg = 0
        # if keynum < 4:
        #     Top3non.append(avg)
        # else:
        #     Fieldnon.append(avg)
            
        # win = temp_pres_percent.count(1)
        # lose = temp_pres_percent.count(0)
        # if win != 0 and lose != 0:
        #     avg = win/(win+lose)
        # else: 
        #     avg = 0
        # if keynum < 4:
        #     Top3pres.append(avg)
        # else:
        #     Fieldpres.append(avg)
        
        loseNon = temp_all_percent.count(0)
        losePres = temp_pres_percent.count(0)
    
        if loseNon != 0 and losePres != 0 and keynum < 4:
            Top3pres.append(losePres/loseNon)
            
        if keynum > 3:
            if loseNon != 0 and losePres != 0:
                Fieldpres.append(losePres/loseNon)
            # else:
            #     print("")
            #     print("BROKEN?")
            #     print(key)
            #     print(loseNon)
            #     print(losePres)
            #     print("")
        
    if key == 'VP':
       VP_pres_List = Top3pres
    if key == 'Fnatic':
        Fnatic_pres_list = Top3pres
    if key == 'Astralis':
        Astralis_pres_list = Top3pres
    if key == 'NaVi':
        NaVi_pres_list = Top3pres
        
    
    if len(Top3pres) != 0:
        Top3PresTotal.append(sum(Top3pres)/len(Top3pres))
    
    if key == 'Fnatic':
        if len(Fnatic_pres_list) != 0:
            FnaticPresTotal = sum(Fnatic_pres_list)/len(Fnatic_pres_list)
            Fnatic_pres_avg = FnaticPresTotal
    if key == 'Astralis':
        if len(Astralis_pres_list) != 0:
            AstralisPresTotal = sum(Astralis_pres_list)/len(Astralis_pres_list)
            Astralis_pres_avg = AstralisPresTotal
    if key == 'NaVi':
        if len(NaVi_pres_list) != 0:
            NaViPresTotal = sum(NaVi_pres_list)/len(NaVi_pres_list)
            NaVi_pres_avg = NaViPresTotal
    if key == 'VP':
        if len(VP_pres_list) != 0:
            VP_presTotal = sum(VP_pres_list)/len(VP_pres_list)
            VP_pres_avg = VPPresTotal
    

    if len(Fieldpres) != 0:
        FieldPresTotal.append(sum(Fieldpres)/len(Fieldpres))
    # Top3pres = [i for i in Top3pres if i != 0]
    # Top3non = [i for i in Top3non if i != 0]
    # Fieldpres = [i for i in Fieldpres if i != 0]
    # Fieldnon = [i for i in Fieldnon if i != 0]
    # if len(Top3pres) != 0 and keynum < 4:
    #     avgPresTop = sum(Top3pres) / len(Top3pres)
    #     Top3PresTotal.append(avgPresTop)
    # if len(Fieldpres) != 0  and keynum > 3:
    #     avgPresField = sum(Fieldpres) / len(Fieldpres)
    #     FieldPresTotal.append(avgPresField)
    # if len(Top3non) != 0 and keynum < 4:
    #     avgNonTop = sum(Top3non) / len(Top3non)
    #     Top3NonPresTotal.append(avgNonTop)
    # if len(Fieldnon) != 0 and keynum > 3:
    #     avgNonField = sum(Fieldnon) / len(Fieldnon)
    #     FieldNonPresTotal.append(avgNonField)
        
    keynum = keynum + 1
    print(key + " is Done!")
avgTop3pres = 0
if len(Top3PresTotal) != 0:
    avgTop3pres = sum(Top3PresTotal)/len(Top3PresTotal)


pressureTest = stats.ttest_1samp(a=FieldPresTotal, popmean=avgTop3pres)


#print("")
#print("Pressure T-Test Data:")
#print(pressureTest)
#print("")

FnatvsAstr_t_test = stats.ttest_1samp(a=Astralis_pres_list, popmean=Fnatic_pres_avg)
FnatvsNaVi_t_test = stats.ttest_1samp(a=NaVi_pres_list, popmean=Fnatic_pres_avg)
AstrvsNaVi_t_test = stats.ttest_1samp(a=NaVi_pres_list, popmean=Astralis_pres_avg)

print("Fnatic vs Astralis T-Test Data:")
print(FnatvsAstr_t_test)
print("")
print("Fnatic vs Na'Vi T-Test Data:")
print(FnatvsNaVi_t_test)
print("")
print("Astralis vs Na'Vi T-Test Data:")
print(AstrvsNaVi_t_test)

print('Top 3 individual vs Field')

#FnatvsField = stats.ttest_ind(Fnatic_pres_total)