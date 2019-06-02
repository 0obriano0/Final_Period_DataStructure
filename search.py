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
    
    def req_vendor(self,select,name):
        return_list = []
        type_list = select.split(' and ')
        for i in range(len(name)):
            line=[]
            for j in type_list:
                line.append(name[i].search(j))
            return_list.append(line)
        return return_list
    
    def require(self,select,data,name):
        if data == 'vendor' :
            return self.req_vendor(select,name)
        elif data == 'product': pass
        else: return 'invalid database name , only vendor and product are available'
    
    def get_all_vendor(self,):
        self.vendor_data = avl.AVLTree()
        data_buffer = []
        data_buffer = FileIO.getalldata("vendor")
        for i in data_buffer:
            self.vendor_data.insert(db.tools.a1z26(i.RN),i)
            self.vendor_dict[i.name] = db.tools.a1z26(i.RN)
        
    def get_all_product(self,):
        self.product_data = avl.AVLTree()
    
    def __init__(self,):
        self.get_all_vendor()
        self.get_all_product()
        print("讀取完成")
        
        
if __name__ == '__main__' :
    search_data = search()
    data = []
    data = search_data.vendor_data.get_all()
    for i in data:
        print(i.name)