# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:26:14 2019

@author: asus
"""

from bs4 import BeautifulSoup
import requests
import FileIO

rs = requests.session()

header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

mainURL = 'https://tw.stock.yahoo.com/d/s/company_'
URL = mainURL

def getnum():
    URL = 'http://www.tej.com.tw/webtej/doc/uid.htm'
    alist = []
    res = rs.get(URL,headers = header)
    res.encoding = 'CP950'
    soup = BeautifulSoup(res.text, "html.parser")
    a = soup.find_all("td" , {"class" : "xl24"})
    for i in range(10000):
        try:
            buffer = a[i].text.split(' ')[0].replace('\xa0','')
        except:
            return alist
        if buffer is not '':
            alist.append(buffer)
    #print(alist)
    return alist
    
    
def getinfo(URL):
    dic = {}
    res = rs.get(URL,headers = header)
    res.encoding = 'CP950'
    soup = BeautifulSoup(res.text, "html.parser")
    a = soup.find_all("td" , {"colspan" : "3"},{"class" : "yui-td-left"})
    title = soup.find("font",{"color":"#F70000"}).findChildren('b')[0].text.replace(' ','')
    dic['principle'] = soup.find_all ("td" , {"align" : "left"})[4].text.replace(' ','')
    dic['RN'] = title[:4]
    dic['name'] = title[4:]
    dic['phonenum'] = a[3].text.replace(' ','')
    dic['address']= a[6].text.replace(' ','')
    dic['product'] = {}
    #print(dic)
    return dic

succes = 0
fail = 0
dicinfo_list = []
for URL in getnum():
    print(mainURL+str(URL)+".html : ", end='')
    try:
        buffer_dict = getinfo(mainURL+str(URL)+".html")
        dicinfo_list.append(buffer_dict)
        FileIO.createYaml(buffer_dict,'vendor')
        succes +=1
        print("成功")
    except :
        fail += 1
        print("失敗")

print("成功: ",succes,"　　失敗:",fail)