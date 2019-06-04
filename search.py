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
    
    fake = {"name":"廠商捌柒","RN":"dddee544442e2","principle":"張先生","address":"新北市","product":[]}
    search_data.createData(fake,'vendor')
    