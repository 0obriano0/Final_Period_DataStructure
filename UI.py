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
    
def postinfo(inputstring):
    dic = {}
    listwords = inputstring.split(' ')
    vendorname = listwords[1].replace('"','').split(',')
    vendor = vendorname[0].split('=')
    item = vendorname[1].split('=')
    quantity = vendorname[2].split('=')
    SN = vendorname[3].split('=')
    if((vendor[0] == 'vendor' or vendor[0] == 'RN') and quantity[0] == 'quantity' and SN[0]=='SN'):
        dic['vendor'] = vendor[1]
        dic[item[0]] = item[1]
        dic[quantity[0]] = int(quantity[1])
        dic[SN[0]] = int(SN[1])
    else:
        print("格式錯誤")
        return(-9999999)
    print(dic)
    return dic

#==================================================#
#input
#==================================================#
if __name__ == '__main__' :
    fakesrting1 = 'select "name","RN" from "vendor" where "name"="UX501VW","rn"="4654654"' #output 'UX501VW' '23638777'
    fakestring2 = 'select * from "vendor" where "name"="ASUS"' #output 'UX501VW' 'ASUS' '23638777' '施先生' '台北市承德路' '26073'
    fakestring3 = 'select "name","address" from "vendor" where "RN"="aasswwwddd555"' #output 'UX501VW' 'ASUS' '23638777' '施先生' '台北市承德路' '26073'
    fakestring4 = 'post "vendor"="一詮","name"="dildo","quantity"="120","SN"="8613213546"'
    fakestring5 = 'pop "vendor"="一詮","name"="dildo","quantity"="12","SN"="8613213546"'
    realstr = 'select "name","RN" from "vendor" where "name"="三洋紡","RN"="1472"'
    
    search_ = sb.search()
    '''a = postinfo(fakestring4)
    search_.insert_product(a)'''
#=================================================#
#
#
#=================================================#
    while(1):
        user_input_str = input("command: ")
        if(user_input_str.split(' ')[0] == 'select'):
            infolist = getinfo(user_input_str)
            info = search_.require(infolist)
            df_data = pd.DataFrame(info, columns = infolist['select'])
            print(df_data)
        elif(user_input_str.split(' ')[0] == 'post'):
            infolist = postinfo(user_input_str)
            search_.insert_product(infolist)
            print(infolist)
        elif(user_input_str.split(' ')[0] == 'pop'):
            infolist = postinfo(user_input_str)
            search_.take_product(infolist)
            print(infolist)
        elif(user_input_str=='exit'):
            print('結束程式')
            break
        else:
            print('輸入錯誤')
            
        
    
    