# -*- coding: utf-8 -*-
"""
Created on Thu May 14 16:55:48 2020

@author: Ismail
"""

import json

ID = int(input(("enter image id: ")))

classes = []

with open('nocaps_val_detections.json','r') as json_file, open('domain.txt','r') as domain:
    data = json.load(json_file)
    domain_list = domain.readlines()
    ids = []
    for cat in data['categories']:
        if cat['id'] in domain_list:
            ids.append(cat['id'])
    print(len(domain_list) == len(ids))
    d = {}
    for i in range(5000):
        d[i] = []
    for ann in data['annotations']:
        d[ann['image_id']].append(ann['category_id'])
        if (ann['image_id']==ID):
            classes.append(ann['category_id'])
    print(classes)
    for cat in data['categories']:
        if cat['id'] in classes:
            print(cat['name'])
    
    for key, value in d.items():
        if (all(item in value for item in ids)):
            print(key)
            