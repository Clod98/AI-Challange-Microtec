# importing the module
import pandas as pd
import datetime
import os
import glob
import numpy as np
  
path = r"C:\Users\39345\Desktop\Microtec challange\boards_2022_04_XX"
csv_files = glob.glob(os.path.join(path, "*.csv"))
big_df = pd.DataFrame()
for f in csv_files:
        
    # reading the files
    boards_info = pd.read_csv(f,encoding='latin-1',sep=';')
    join_file = pd.read_excel(r"C:\Users\39345\Desktop\Microtec challange\BoardInfoNew.xlsx")
    join_file = join_file.rename(columns={"Unnamed: 9":"Number"})
 
    #joining the files
    df = pd.merge(boards_info,join_file, how = "inner",on = ["Number"])
    df.set_index("Number")
    # print(df["Id	Time	Delta [ms]	"])
    df[["id","date","time","delta"]]= df["Id	Time	Delta [ms]	"].str.split(n = 3,expand = True)
    df[["time","useless","uselessagain"]] = df["time"].str.rsplit(pat=":",n=2,expand=True)
    df = df.rename(columns = {"Unnamed: 10":"date2"})
    df["date2"] = df["date2"].astype(str)
    df[["date2","time2"]] = df["date2"].str.split(n=1,expand=True)
    df[["time2","useless2"]] = df["time2"].str.rsplit(pat=":",n=1,expand=True)
    # print(df.columns)
    # break

    df["fullId"]=(df["Unnamed: 1"].astype(str)+df["Unnamed: 2"].astype(str).str.zfill(2)).astype(np.int64)
    df = df.loc[ (pd.to_datetime(df['date2'],format='%Y-%m-%d') - pd.to_datetime(df['date'],format="%Y:%m:%d")).abs() <= datetime.timedelta(days=0)]
    df = df.loc[ (pd.to_datetime(df['time2']) - pd.to_datetime(df['time'])).abs() <= datetime.timedelta(hours=1)]
    big_df = pd.concat([big_df,df])
    # print(df)
big_df = big_df[["Unnamed: 1","Number",big_df.columns[55],"fullId"]]
big_df = big_df.rename(columns={"Unnamed: 1":"IdLog"})
big_df.to_excel(r"C:\Users\39345\Desktop\Microtec challange\JointDataset2.xlsx")
# print(len(big_df))
# print(len(join_file.axes[0]))
# print(len(join_file.axes[1]))
# print(len(df.axes[0]))
# print(len(df.axes[1]))
# print(df.size)