# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:44:55 2022

@author: Tabriz
"""

# import pandas as pd
# df = pd.read_csv("./BoardInfoNew.csv") 
# print(df)


import pandas as pd

# Read the files into two dataframes.
df1 = pd.read_excel(r"C:\Users\39345\Desktop\Microtec challange\JointDataset2.xlsx")
df2 = pd.read_csv(r"C:\Users\39345\Desktop\Microtec challange\mats.csv")

# Merge the two dataframes, using _ID column as key
df3 = pd.merge(df1, df2, left_on = 'IdLog',right_on="LogID")
df3.set_index('LogID', inplace = True)

# Write it to a new CSV file
df3.to_csv('final2.csv')
