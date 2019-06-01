# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(show8301)s
"""

class vendor():
    name = ""
    number = 0
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
            self.number = data_dict["number"]
            self.RN = data_dict["RN"]
            self.principle = data_dict["principle"]
            self.address = data_dict["address"]
            self.product = data_dict["product"]
        
    def search(self,type_str):
        if type_str == "name":
            return self.name
        elif type_str == "number":
            return self.number
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
                
    def info(self): return [self.name,self.number,self.principle,self.principle,self.address,self.RN,self.product]
        
class product():
    number = ""
    name = ""
    SN = ""
    warranty = ""
    volume = ""
    weight = 0
    category = ""
    
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
        
    def search(self,type_str):
        if type_str == "number":
            return self.number
        elif type_str == "name":
            return self.name
        elif type_str == "SN":
            return self.SN
        elif type_str == "warranty":
            return self.warranty
        elif type_str == "volume":
            return self.volume
        elif type_str == "weight":
            return self.weight
        elif type_str == "category":
            return self.category
        else:
            return None
        
    def info(self): return [self.number,self.name,self.SN,self.warranty,self.volume,self.weight,self.category]
