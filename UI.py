# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:06:37 2019

@author: asus
"""
import pandas as pd
import search as sb
import time
import os


def getinfo(inputstring):
    listwords = inputstring.split(" ")
    if(listwords[0]=='select' and listwords[2]=='from' and listwords[4] == 'where'):
        dic = {}
        dicwhere = {} 
        select_ = listwords[1].replace('"','').split(',')
        from_ = listwords[3].replace('"','')
        where_ = listwords[5].replace('"','').split(',')
        for i in where_:
            if "=" not in i:
                return -999999999
            buffer = i.split('=')
            dicwhere[buffer[0]] = buffer[1]
        if select_[0] == "*":
            if from_ == "vendor":
                dic['select'] = ['name','RN','principle','address','product']
            elif from_ == "product":
                dic['select'] = ['name','SN','number','warranty','volume','weight','category','quantity']
        else:
            dic['select'] = select_
        dic['from'] = from_
        dic['where'] = dicwhere
        return dic
    else:
        return(-999999999)
    
def post_popinfo(inputstring):
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
    #print(dic)
    return dic

#==================================================#
#input
#==================================================#
if __name__ == '__main__' :
    fakesrting1 = 'select "name","RN" from "vendor" where "name"="UX501VW","rn"="4654654"'
    fakestring2 = 'select * from "vendor" where "name"="ASUS"' 
    fakestring3 = 'select "name","address" from "vendor" where "RN"="aasswwwddd555"' 
    fakestring4 = 'post "vendor"="一詮","name"="dildo","quantity"="120","SN"="8613213546"'
    fakestring5 = 'pop "vendor"="一詮","name"="dildo","quantity"="12","SN"="8613213546"'
    realstr = 'select "name","RN" from "vendor" where "name"="三洋紡","RN"="1472"'
    
    search_ = sb.search()
#=================================================#
#
#
#=================================================#
    while(1):
        print("\n=====================================================")
        user_input_str = input("command: ")
        
        check_button = 1
        
        if user_input_str != "exit":
            for check_data in [' ','"']:
                if check_data not in user_input_str:
                    check_button = 0
                    break
            if check_button == 0:
                print('輸入錯誤')
                continue
        
        if(user_input_str.split(' ')[0] == 'select'):
            infolist = getinfo(user_input_str)
            if infolist == -999999999:
                print('輸入錯誤')
                continue
            info = search_.require(infolist)
            if info == []:
                print('查無資料')
                continue
            df_data = pd.DataFrame(info, columns = infolist['select'])
            df_data.to_csv('./outputFile/' + time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()) + '.csv', encoding='utf_8_sig', index = False)
            print(df_data)
            print("FileCreate: ",os.getcwd(),"/" + time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()) + '.csv')
        elif(user_input_str.split(' ')[0] == 'post'):
            try:
                infolist = post_popinfo(user_input_str)
            except:
                print('輸入錯誤')
                continue
            search_.insert_product(infolist)
            print("input command(post):",infolist)
        elif(user_input_str.split(' ')[0] == 'pop'):
            try:
                infolist = post_popinfo(user_input_str)
            except:
                print('輸入錯誤')
                continue
            search_.take_product(infolist)
            print("input command(pop):",infolist)
        elif(user_input_str=='exit'):
            print('結束程式')
            break
        else:
            print('輸入錯誤')
            
        
    
    