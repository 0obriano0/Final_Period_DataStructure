# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:27:48 2019

@author: brian
"""
import database
import yaml
    
#=============================== function =================================
def LoadYaml(url):
    try:
        with open(url, "r", encoding="utf-8") as stream:
            data = yaml.load(stream)
    except:
        data = None
    return data

def LoadData(name,typeSelect):
    typeCheck = ["vendor","product"]
    if typeSelect not in typeCheck:
        return None
    load_data = LoadYaml("./" + typeSelect + "/" + name)
    if load_data is not None:
        if typeSelect in load_data:
            return load_data[typeSelect]
        print("檔案讀取失敗，格式錯誤")
    else:
        print("查無此檔案")
    return None

def formatVendor(data_dict):
    return database.vendor(data_dict["name"],data_dict["RN"],data_dict)

def formatVendor_list(data_list):
    final = []
    for data_ in data_list:
        final.append(formatVendor())
    return final
    
#=============================== main =================================
if __name__ == '__main__':
    #=============================== test =================================
    data_dict = LoadData("聲寶.yml","vendor")
    a = formatVendor(data_dict)
    print(a.principle)