# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:27:48 2019

@author: brian
"""
import os
import database
import pandas as pd
import yaml
    
#=============================== function =================================
def loadFile(url):
    if os.path.isfile(url):
        df = pd.read_csv(url)
    else:
        if "vendor" in url:
            NewList = [["","","","","",""]]
            columns_list = ["name","number","principle","address","RN","product"]
        else:
            NewList = ["","","","","","",""]
            columns_list = ["number","name","SN","warranty","volume","weight","category"]
        df = pd.DataFrame(NewList, columns = columns_list)
        df.to_csv(url,encoding='utf_8_sig' , index = False)
    return df

def LoadYaml(url):
    with open(url, “r”) as stream:
    data = yaml.load(stream)

def loadvendor():
    loadFile("./vendor.csv")

def loadproduct():
    loadFile("./product.csv")

def updata(data_tpye,data_database):
    

def upload
    
#=============================== main =================================
if __name__ == '__main__':
    #=============================== test =================================
    list_data = []
    
    for index in range(5):
        a = database.vendor("brian",123456)
        list_data.append(a)
        
    list_data[0].name = "a"
    list_data[0].RN = 123456789654
        
    
    print(list_data[0].name)
    
    print(list_data[1].name)
    loadvendor()