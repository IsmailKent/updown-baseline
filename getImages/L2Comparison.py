# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:15:29 2020

@author: Ismail
"""

"""
Steps:
    1- find 2 boxes with same class id 
    2- find their features
    3- compare their L2 distance
"""


import json



with open('nocaps_val_detections.json','r') as oi_result:
    results = json.load(oi_result)
    print(results['categories'])