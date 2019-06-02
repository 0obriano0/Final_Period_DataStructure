# -*- coding: utf-8 -*-
"""
Created on Wed May 22 21:22:51 2019

@author: brian
"""

import database as db
import search

list_data = []

list_data.append(db.vendor('alskdjf',154153))
list_data.append(db.vendor('aasdfjf',15456.353))
list_data.append(db.vendor('abtab',546.))
list_data.append(db.vendor('ahjkjkghj',5463456))
list_data.append(db.vendor('mnvfxd',63545653))
list_data.append(db.vendor('ew4rghe',7837483))
list_data.append(db.vendor('r5yebnr',77154153))

search_data = search.search()
data = []
data = search_data.vendor_data.get_all()
for i in data:
    print(i.name)