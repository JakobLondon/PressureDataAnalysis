# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 14:06:06 2022

@author: Jakob
"""
from statsmodels.stats.weightstats import ztest as ztest
import pandas as pd
import numpy as np
import scipy.stats as stats
from csv import reader
import pickle
import tarfile

# open a .spydata file
filename = 'CSGOField.spydata'
tar = tarfile.open(filename, "r")
# extract all pickled files to the current working directory
tar.extractall()
extracted_files = tar.getnames()
for f in extracted_files:
    if f.endswith('.pickle'):
          with open(f, 'rb') as fdesc:
              CSGO_data = pickle.loads(fdesc.read())
# or use the spyder function directly:
from spyder_kernels.utils.iofuncs import load_dictionary
Field_pres_total = CSGO_data['FieldPresTotal']

# open a .spydata file
filename = 'TennisField.spydata'
tar = tarfile.open(filename, "r")
# extract all pickled files to the current working directory
tar.extractall()
extracted_files = tar.getnames()
for f in extracted_files:
    if f.endswith('.pickle'):
          with open(f, 'rb') as fdesc:
              Tennis_data = pickle.loads(fdesc.read())
# or use the spyder function directly:
from spyder_kernels.utils.iofuncs import load_dictionary
Field_df_list = Tennis_data['Field_df_avgs']
Field_df_list = list(filter(lambda num: num != 0.0, Field_df_list))
Field_bp_list = Tennis_data['Field_bp_list']


Tennis_df = [0.01834862385,0.00680272108,0.0178041543]
Tennis_bp = [0.5790352573133482, 0.56209540928161, 0.5692120397950574]
CSGOTop3 = [0.3408122413498871, 0.40628765954960044, 0.36162145314839317]

print("Tennis Double Fault Top 3 vs CSGO Top 3:")


TennisDFvsCSGOTop3 = stats.ttest_ind(Tennis_df,CSGOTop3)
Z_TennisDFvsCSGOTop3 = ztest(Tennis_df,CSGOTop3)
print(TennisDFvsCSGOTop3)
print("")
print("Tennis Break Point Top 3 vs CSGO Top 3:")
TennisBPvsCSGOTop3 = stats.ttest_ind(Tennis_bp,CSGOTop3)
Z_TennisBPvsCSGOTop3 = ztest(Tennis_bp,CSGOTop3)
print(TennisBPvsCSGOTop3)
print('')
print("Tennis Double Fault Field vs CSGO Field")
TennisDFFieldvsCSGOField = stats.ttest_ind(Field_df_list,Field_pres_total)
Z_TennisDFFieldvsCSGOField = ztest(Field_df_list,Field_pres_total)
print(TennisDFFieldvsCSGOField)
print("")
print("Tennis Break Point Field vs CSGO Field")
TennisBPFieldvsCSGOField = stats.ttest_ind(Field_bp_list,Field_pres_total)
Z_TennisBPFieldvsCSGOField = ztest(Field_bp_list,Field_pres_total)
print(TennisBPFieldvsCSGOField)

CSGO_field_list = CSGO_data['FieldPresTotal']

Astralis_avg = CSGO_data['Astralis_pres_avg']
Astralis_list = CSGO_data['Astralis_pres_list']

Fnatic_avg = CSGO_data['Fnatic_pres_avg']
Fnatic_list = CSGO_data['Fnatic_pres_list']

NaVi_avg = CSGO_data['NaVi_pres_avg']
NaVi_list = CSGO_data['NaVi_pres_list']

VP_list = CSGO_data['VP_pres_List']
VP_avg = sum(VP_list)/len(VP_list)

Astralis_VP_avg = (Astralis_avg+VP_avg)/2
NaVi_VP_avg = (NaVi_avg+VP_avg)/2
Astralis_NaVi_avg = (Astralis_avg+NaVi_avg)/2

Top3_csgo_avg = (Astralis_avg+NaVi_avg+VP_avg)/3

AstralisvsTop3 = stats.ttest_1samp(a=Astralis_list, popmean=NaVi_VP_avg)
VPvsTop3 = stats.ttest_1samp(a=VP_list, popmean=Astralis_NaVi_avg)
NaVivsTop3 = stats.ttest_1samp(a=NaVi_list, popmean=Astralis_VP_avg)

Z_AstralisvsTop3 = ztest(Astralis_list,value = NaVi_VP_avg)
Z_VPvsTop3  = ztest(VP_list,value = Astralis_NaVi_avg)
Z_NaVivsTop3 = ztest(NaVi_list,value = Astralis_VP_avg)

CSGO_Top3vsField = stats.ttest_1samp(a=CSGO_field_list, popmean=Top3_csgo_avg)

Z_CSGO_Top3vsField = ztest(CSGO_field_list,value = Top3_csgo_avg)

AstralisvsField = stats.ttest_1samp(a=CSGO_field_list, popmean=Astralis_avg)
VPvsField = stats.ttest_1samp(a=CSGO_field_list, popmean=VP_avg)
NaVivsField = stats.ttest_1samp(a=CSGO_field_list, popmean=NaVi_avg)

Z_AstralisvsField = ztest(CSGO_field_list,value = Astralis_avg)
Z_VPvsField = ztest(CSGO_field_list,value = VP_avg)
Z_NaVivsField = ztest(CSGO_field_list,value = NaVi_avg)

print("")
print("Astralis vs (VP and Na'Vi)")
print(AstralisvsTop3)
print("")
print("VP vs (Astralis and Na'Vi)")
print(VPvsTop3)
print("")
print("Na'Vi vs (VP and Astralis)")
print(NaVivsTop3)
print("")
print("Top 3 CSGO vs Field CSGO")
print(CSGO_Top3vsField)
print("")
print("Astralis vs Field")
print(AstralisvsField)
print("")
print("VP vs Field")
print(VPvsField)
print("")
print("Na'Vi vs Field")
print(NaVivsField)
print("")


