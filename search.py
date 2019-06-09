# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:55:56 2019

@author: b2787
"""
#select RN and number from vendor where name = brian

import database as db
import FileIO
import avl_tree as avl
import pandas as pd

class search():
    vendor_data = avl.AVLTree()
    product_data = avl.AVLTree()
    vendor_dict = {}
    product_dict = {} 
    
    def get_all_vendor(self,):
        self.vendor_data = avl.AVLTree()
        data_buffer = []
        data_buffer = FileIO.getalldata("vendor")
        for i in data_buffer:
            self.vendor_data.insert(db.tools.a1z26(i.RN),i)
            self.vendor_dict[i.name] = db.tools.a1z26(i.RN)

    def get_all_product(self,):
        self.product_data = avl.AVLTree()
        data_buffer = []
        data_buffer = FileIO.getalldata("product")
        for i in data_buffer:
            self.product_data.insert(db.tools.a1z26(i.SN),i)
            self.product_dict[i.name] = db.tools.a1z26(i.SN)
        self.product_data.last_num = FileIO.last_num
    
    def insert_product(self,data_dict):
        if 'name' in data_dict:
            product = data_dict['name']
            vendor = ""
            if 'No' in data_dict:
                vendor = data_dict['No']
            elif 'vendor' in data_dict:
                vendor = data_dict['vendor']
            else:
                return -9
            if vendor in self.vendor_dict:
                product_data_ = None
                getvendor = self.vendor_data.search(self.vendor_dict[vendor])
                if product in getvendor.product:
                    product_data_ = self.product_data.search(getvendor.product[product])
                    if product_data_.SN != data_dict['SN']:
                        #print("資料名稱 跟 商品條碼不符合")
                        return -4
                    FileIO.remove(str(product_data_.SN),'product')
                else:
                    self.product_data.last_num += 1
                    from copy import deepcopy
                    data = deepcopy(self.product_data.last_num)
                    product_data_ = db.product(product,data_dict['SN'])
                    product_data_.number = deepcopy(data)
                    product_data_.SN = data_dict['SN']
                    getvendor.product[product] = product_data_.SN
                    FileIO.remove(getvendor.name,'vendor')
                    FileIO.createYaml(getvendor,'vendor')
                    self.product_dict[product] = product_data_.SN 
                    self.product_data.insert(product_data_.SN,product_data_)
                product_data_.quantity+=data_dict['quantity']
                #print("fileIO = ",FileIO.createYaml(product_data_,'product'))
                FileIO.createYaml(product_data_,'product')
                return 1
        return -1
    def take_product(self,data_dict):
        if 'name' in data_dict:
            product = data_dict['name']
            vendor = ""
            if 'No' in data_dict:
                vendor = data_dict['No']
            elif 'vendor' in data_dict:
                vendor = data_dict['vendor']
            else:
                return -9
            if vendor in self.vendor_dict:
                product_data_ = None
                getvendor = self.vendor_data.search(self.vendor_dict[vendor])
                if product in getvendor.product:
                    product_data_ = self.product_data.search(getvendor.product[product])
                    if product_data_.quantity >= data_dict['quantity']:
                        FileIO.remove(str(product_data_.SN),'product')
                        product_data_.quantity-=data_dict['quantity']
                        FileIO.createYaml(product_data_,'product')
                    else:
                        #print("提取數量大於庫存數量")
                        return -2
                else:
                    #print("查無此商品")
                    return -3
            
    
    def createData(self,data_dict,typeSelect):
        if typeSelect == 'vendor':
            item = FileIO.formatDatabase(data_dict,typeSelect)
            debug = FileIO.createYaml(item,typeSelect)
            if debug == 1:
                self.vendor_data.insert(db.tools.a1z26(item.RN),item)
                self.vendor_dict[item.name] = db.tools.a1z26(item.RN)
            else: return debug
        elif typeSelect == 'product':
            item = FileIO.formatDatabase(data_dict,typeSelect)
            debug = FileIO.createYaml(item,typeSelect)
            if debug == 1: 
                self.product_data.insert(db.tools.a1z26(item.SN),item)
                self.product_dict[item.name] = db.tools.a1z26(item.SN)
            else: return debug
            
    def removeData(self,data_name,typeSelect):
        if typeSelect == 'vendor':
            if data_name in self.vendor_dict.keys():
                if FileIO.remove(data_name,typeSelect) == 0:
                    self.vendor_data.delete(data_name)
                    self.vendor_dict.pop(data_name)
                else:
                    return FileIO.remove(data_name,typeSelect)
        elif typeSelect == 'product':
            if data_name in self.product_dict.keys():
                if FileIO.remove(data_name,typeSelect) == 0:
                    self.product_data.delete(data_name)
                    self.product_dict.pop(data_name)
                else:
                    return FileIO.remove(data_name,typeSelect)
                
    def getName(self,number,typeSelect):
        try:
            listOfKeys = list()
            listOfItems = eval('self.'+typeSelect+'_dict.items()')
            for item  in listOfItems:
                if item[1] == db.tools.a1z26(number):
                    listOfKeys.append(item[0])
            return  listOfKeys
        except: 
            #print('dict找不到number的key')
            return -1
            
    def require(self,data):
        return_list = []
        attribute = []
        keys = []
        all_vatt = ['name','RN','principle','address','product']
        all_patt = ['name','SN','number','warranty','volume','weight','category','quantity']
        attribute = data['select']
        keys = data['where'].keys()
        if data['from'] == 'vendor':
            for key in keys:
                vdata  = self.vendor_data.search(key,data['where'][key])
                for v in vdata:
                    inside_return_list = []
                    if '*' in attribute:
                        attribute = all_vatt
                    for att in attribute:
                        inside_return_list.append(eval('v.' + att))      
                    if len(inside_return_list) > 0 :
                        return_list.append(inside_return_list)
            return return_list
        elif data['from'] == 'product':
            for key in keys:
                pdata  = self.product_data.search(key,data['where'][key])
                for p in pdata:
                    inside_return_list = []
                    if '*' in attribute:
                        attribute = all_patt
                    for att in attribute:
                        inside_return_list.append(eval('p.' + att))  
                    if len(inside_return_list) > 0 :
                        return_list.append(inside_return_list)
            return return_list
    
    def __init__(self,):
        self.get_all_vendor()
        self.get_all_product()
        print("讀取完成")
        
        
if __name__ == '__main__' :
    search_data = search()
    vdata = []
    pdata = []
    vdata = search_data.vendor_data.get_all()
    pdata = search_data.product_data.get_all()

    '''
    for i in vdata:
        print(i.name)
    for i in pdata:
        print(i.name)
    print(search_data.vendor_dict,search_data.product_dict)
    '''
    '''
    
    fake = {"name":"廠商捌柒","RN":"dddddee544442e2","principle":"張先生","address":"新北市","product":[]}
    search_data.createData(fake,'vendor')
    abcdefg = search_data.require({'select': ['*'], 'from': 'vendor', 'where': {'RN': '1472'}})
    abcde = search_data.require({'select':['*'],'from':'vendor','where':{'name':'廠商捌柒'}})
    print(abcdefg)
    print(abcde)
    print(search_data.getName("dddee544442e2",'vendor'))
    '''
    search_data.insert_product({'name':"火車",'vendor':"一詮","quantity":2,"SN":12345678996})
    search_data.insert_product({'name':"火車2",'vendor':"一詮","quantity":2,"SN":1234558996})
    search_data.insert_product({'name':"火車4",'vendor':"一詮","quantity":2,"SN":1234565558996})
    search_data.insert_product({'name':"火車5",'vendor':"一詮","quantity":2,"SN":12345555895})
    search_data.insert_product({'name':"火車6",'vendor':"一詮","quantity":2,"SN":1234567556})
    search_data.take_product({'name':"火車6",'vendor':"一詮","quantity":3,"SN":1234567556})