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
        except: #print('dict找不到number的key')
            return -1
            
    def require(self,data):
        return_list = []
        attribute = []
        keys = []
        all_att = ['name','RN','principle','address','product']
        attribute = data['select']
        keys = data['where'].keys()
        if data['from'] == 'vendor':
            for key in keys:
                vdata  = self.vendor_data.search(key,data['where'][key])
                for v in vdata:
                    inside_return_list = []
                    if '*' in attribute:
                        for att in all_att:
                            inside_return_list.append(eval('v.' + att))
                    else:
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
                        for att in all_att:
                            inside_return_list.append(eval('p.' + att))
                    else:
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
    for i in vdata:
        print(i.name)
    for i in pdata:
        print(i.name)
    print(search_data.vendor_dict,search_data.product_dict)
    
    fake = {"name":"廠商捌柒","RN":"dddddee544442e2","principle":"張先生","address":"新北市","product":[]}
    search_data.createData(fake,'vendor')
    abcde = search_data.require({'select':['RN'],'from':'vendor','where':{'name':'廠商捌柒'}})
    print(abcde)
    print(search_data.getName("dddee544442e2",'vendor'))
    