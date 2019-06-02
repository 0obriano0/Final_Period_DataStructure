# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:55:56 2019

@author: b2787
"""
#select RN and number from vendor where name = brian

import database 
import avl_tree as avl
import pandas as pd

global vendor_data
global product_data

    
def require(select,data,name):
    if data == 'vendor' :
        return req_vendor(select,name)
    elif data == 'product': pass
    else: return 'invalid database name , only vendor and product are available'
    

def req_vendor(select,name):
    return_list = []
    type_list = select.split(' and ')
    for i in range(len(name)):
        line=[]
        for j in type_list:
            line.append(name[i].search(j))
        return_list.append(line)
    return return_list

def get_all_vendor():
    vendor_data = avl.AVLTree()
    
def get_all_product():
    product_data = avl.AVLTree()
    
    
    
    
    
    
    
def __init__(self):
    get_all_vendor()
    get_all_product()