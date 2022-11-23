import cv2
import pandas as pd
import numpy  as np
import os
from tqdm import tqdm

fold = "C:/Users/39345/Desktop/Microtec challange/exportBrd/"


ext = list(range(0,29))
columns = ["LogID"]
columns.extend(ext)
df = pd.DataFrame(columns=columns)

for fname in tqdm(os.listdir(fold)):
    
    images = []
    
    # print(fname)
    images = cv2.imreadmulti(mats = images, filename = fold + fname, flags = cv2.IMREAD_ANYCOLOR + cv2.IMREAD_ANYDEPTH)
    
    # print(images[0])
    # print("************************")
    # print(len(images[1]))
    # print()
    #for i in range(0,len(images[1])):
    
    logid = fname.split("@")[1].split(".")[0]
    
    # sw_dens_mean = round(np.mean(images[1][14][1]),3)
    # hw_dens_mean = round(np.mean(images[1][14][2]),3)
    # pith_dev_mean = round(np.mean(images[1][14][5]),3)
    
    new_row = {'LogID': logid}
    

    for i in range(0,29):
        new_value = round(np.mean(images[1][14][i]),3)
        new_row[i] = new_value
        
    # print(logid)
    # print(sw_dens_mean)
    # print(hw_dens_mean)
    # print(pith_dev_mean)
    
#append row to the dataframe
    df = df.append(new_row, ignore_index=True)
    

print(df)
df.to_csv(".csv", index=False)

'''
    for i in range(14, 14+1):
        
        print(np.mean(images[1][i][1]))
        print(images[1][i].shape)
        
    print("*************************")
    print(images[1][15].dtype)
'''