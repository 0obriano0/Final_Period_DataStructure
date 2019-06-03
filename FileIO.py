# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:27:48 2019

@author: brian
"""
import database
import yaml
#=============================== function =================================
def loadYaml(url):
    try:
        with open(url, "r", encoding="utf-8") as stream:
            data = yaml.load(stream)
    except:
        data = None
    return data

def loadData(name,typeSelect):
    typeCheck = ["vendor","product"]
    if typeSelect not in typeCheck:
        return None
    load_data = loadYaml("./" + typeSelect + "/" + name + ".yml")
    if load_data is not None:
        if typeSelect in load_data:
            return load_data[typeSelect]
        print("檔案讀取失敗，格式錯誤")
    else:
        print("查無此檔案")
    return None

def createYaml(data_database,typeSelect):
    final_dict = {}
    url = ""
    if data_database is not None:
        secand_dict = {}
        if typeSelect  == "vendor":
            url = "./" + typeSelect + "/" + data_database.name + ".yml"
            if loadYaml(url) is not None:
                #print("此檔案已經存在")
                return -1
            secand_dict["name"] = data_database.name
            secand_dict["RN"] = data_database.RN
            secand_dict["principle"] = data_database.principle
            secand_dict["address"] = data_database.address
            secand_dict["product"] = data_database.product
        elif typeSelect == "product":
            url ="./" + typeSelect + "/" + data_database.number + ".yml"
            if loadYaml(url) is not None:
                #print("此檔案已經存在")
                return -1
            secand_dict["name"] = data_database.name
            secand_dict["number"] = data_database.number
            secand_dict["SN"] = data_database.SN
            secand_dict["warranty"] = data_database.warranty
            secand_dict["volume"] = data_database.volume
            secand_dict["weight"] = data_database.weight
            secand_dict["category"] = data_database.category
        else:
            #print("傳進來的資料結構有問題")
            return -2
        final_dict[typeSelect] = secand_dict
        with open(url, 'w', encoding="utf-8") as outfile:
            yaml.dump(final_dict, outfile, default_flow_style=False, encoding=('utf-8'), allow_unicode=True)
        return 1
    else:
        #print("傳入的資料結構是: None")
        return 0

def formatDatabase(data_dict,typeSelect):
    if typeSelect == "vendor":
        return database.vendor(data_dict["name"],data_dict["RN"],data_dict)
    elif typeSelect == "product":
        return database.vendor(data_dict["name"],data_dict["SN"],data_dict)

def formatDatabase_list(data_list,typeSelect):
    final = []
    for data_ in data_list:
        final.append(formatDatabase(data_,typeSelect))
    return final

def getalldata(typeSelect):
    a = []
    if typeSelect == "vendor":
        a.append(formatDatabase({"name":"廠商一","RN":"dddee544442e2","principle":"張先生","address":"新北市","product":[]},"vendor"))
        a.append(formatDatabase({"name":"廠商二","RN":"ddddwe5545d22e2","principle":"張小姐","address":"台北市","product":[]},"vendor"))
        a.append(formatDatabase({"name":"廠商三","RN":"dwwwd55555666e2","principle":"黃先生","address":"台中市","product":[]},"vendor"))
        a.append(formatDatabase({"name":"廠商四","RN":"dddee5555889swwe2","principle":"鄭先生","address":"高雄市","product":[]},"vendor"))
    elif typeSelect == "product":
        a.append(formatDatabase({"name":"49吋螢幕","SN":1234564658,"warranty":"2019-02-05","weight":50,"volume":100,"category":"電腦周邊"},"product"))
        a.append(formatDatabase({"name":"i7 電腦","SN":4556321548,"warranty":"2089-02-05","weight":400,"volume":200,"category":"電腦"},"product"))
        a.append(formatDatabase({"name":"鍵盤","SN":45165748777,"warranty":"2019-12-05","weight":500,"volume":300,"category":"電腦周邊"},"product"))
        a.append(formatDatabase({"name":"耳機","SN":5468785213215,"warranty":"2012-05-31","weight":1000,"volume":400,"category":"電腦周邊"},"product"))
    return a
    
#=============================== main =================================
if __name__ == '__main__':
    #=============================== test =================================
    #讀取檔案---------------------------------範例
    a = []
    data_dict = loadData("聲寶","vendor")
    a.append(formatDatabase(data_dict,"vendor"))
    print(a[0].principle)
    
    #利用完整的檔案來做輸出/讀取---------------範例
    a[0].name = "abc"
    createYaml(a[0],"vendor")
    data_dict = loadData("abc","vendor")
    a.append(formatDatabase(data_dict,"vendor"))
    
    #利用創造出來的檔案來做輸出/讀取-----------範例
    b = database.vendor("廠商一","123456789")
    createYaml(b,"vendor")
    data_dict = loadData("廠商一","vendor")
    a.append(formatDatabase(data_dict,"vendor"))
    
    data_num = 0
    data_num = database.tools.a1z26("zAb")
    print("ddd",a[0].search("name"))