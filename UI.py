# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:06:37 2019

@author: asus
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics

def getinfo(inputstring):
    listwords = inputstring.split(" ")
    print(listwords)
    if(listwords[0]=='select' and listwords[2]=='from' and listwords[4] == 'where'):
        dic = {}
        dicwhere = {} 
        print('selecting')
        select_ = listwords[1].replace('"','').split(',')
        from_ = listwords[3].replace('"','')
        where_ = listwords[5].replace('"','').split(',')
        print(where_)
        for i in where_:
            buffer = i.split('=')
            dicwhere[buffer[0]] = buffer[1]
            print(dicwhere)
    else:
        print("語法錯誤")
    
#==================================================#
#input
#==================================================#
fakesrting1 = 'select "name","RN" from "vender" where "name"="UX501VW","rn"="4654654"' #output 'UX501VW' '23638777'
fakestring2 = 'select * from "vendor" where "name" = "ASUS"' #output 'UX501VW' 'ASUS' '23638777' '施先生' '台北市承德路' '26073'
fakestring3 = 'select * from "vendor" where "RN" = "23638777"' #output 'UX501VW' 'ASUS' '23638777' '施先生' '台北市承德路' '26073'


a = {"select":["name","RN"],"from":"vendor","where":{"name":"UX501VM"}}
a = getinfo(fakesrting1)