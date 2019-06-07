# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(show8301)s
"""

class vendor:
    name = ""
    RN = 0
    principle = ""
    address = ""
    product = {}
    
    def __init__(self,name,RN,data_dict = None):
        if data_dict is None:
            self.name = name
            self.RN = RN
        else:
            self.name = data_dict["name"]
            self.RN = data_dict["RN"]
            self.principle = data_dict["principle"]
            self.address = data_dict["address"]
            self.product = data_dict["product"]
        
    def search(self,type_str):
        return eval("self." + type_str)
        '''
        if type_str == "name":
            return self.name
        elif type_str == "RN":
            return self.RN
        elif type_str == "principle":
            return self.principle
        elif type_str == "address":
            return self.address
        elif type_str == "product":
            return self.product
        else:
            return None
        '''
                
    def info(self): return [self.name,self.principle,self.principle,self.address,self.RN,self.product]
        
class product:
    number = ""
    name = ""
    SN = ""
    warranty = ""
    volume = ""
    weight = 0
    category = ""
    quantity = 0
    
    def __init__(self,name,SN,data_dict = None):
        if data_dict is None:
            self.name = name
            self.SN = SN
        else:
            self.number = data_dict["number"]
            self.name = data_dict["name"]
            self.SN = data_dict["SN"]
            self.warranty = data_dict["warranty"]
            self.volume = data_dict["volume"]
            self.weight = data_dict["weight"]
            self.category = data_dict["category"]
            self.quantity = data_dict["quantity"]
            
    def search(self,type_str):
        return eval("self." + type_str)
        
    def info(self): return [self.number,self.name,self.SN,self.warranty,self.volume,self.weight,self.category,self.quantity]

class tools:
    def a1z26(str_data):
        str_data = str(str_data)
        final_str_data = ""
        for char_data in str_data:
            if ord(char_data) >= ord("0") and ord(char_data) <= ord("9"):
                final_str_data = final_str_data + char_data
            elif ord(char_data) >= ord("a") and ord(char_data) <= ord("z"):
                final_str_data = final_str_data + str(ord(char_data) - ord("a"))
            elif ord(char_data) >= ord("A") and ord(char_data) <= ord("Z"):
                final_str_data = final_str_data + str(ord(char_data) - ord("A")+26)
        return int(final_str_data)