# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:06:37 2019

@author: asus
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics
import pandas as pd
import search as sb


def getinfo(inputstring):
    listwords = inputstring.split(" ")
    #print(listwords)
    if(listwords[0]=='select' and listwords[2]=='from' and listwords[4] == 'where'):
        dic = {}
        dicwhere = {} 
        select_ = listwords[1].replace('"','').split(',')
        from_ = listwords[3].replace('"','')
        where_ = listwords[5].replace('"','').split(',')
        for i in where_:
            buffer = i.split('=')
            dicwhere[buffer[0]] = buffer[1]
        dic['select'] = select_
        dic['from'] = from_
        dic['where'] = dicwhere
        #print(dic)
        return dic
    else:
        #print("語法錯誤")
        return(-999999999)
    
#==================================================#
#input
#==================================================#
if __name__ == '__main__' :
    fakesrting1 = 'select "name","RN" from "vendor" where "name"="UX501VW","rn"="4654654"' #output 'UX501VW' '23638777'
    fakestring2 = 'select * from "vendor" where "name"="ASUS"' #output 'UX501VW' 'ASUS' '23638777' '施先生' '台北市承德路' '26073'
    fakestring3 = 'select "name","address" from "vendor" where "RN"="aasswwwddd555"' #output 'UX501VW' 'ASUS' '23638777' '施先生' '台北市承德路' '26073'
    realstr = 'select "name","RN" from "vendor" where "name"="三洋紡","RN"="1472"'
    user_input_str = input("command: ")
    search_ = sb.search()
    a = getinfo(user_input_str)
    info = search_.require(a)
    
    df_data = pd.DataFrame(info, columns = a['select'])
    print(df_data)