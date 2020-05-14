# -*- coding: utf-8 -*-
"""
Created on Thu May 14 16:55:48 2020

@author: Ismail
"""

import json
import os

ID = int(input(("enter image id: ")))

file_source = "nocaps_val_detections.json"

classes = []
with open(file_source) as json_file:
    data = json.load(json_file)
    for ann in data['annotations']:
        if (ann['image_id']==ID):
            classes.append(ann['category_id'])
    print(classes)
    for cat in data['categories']:
        if cat['id'] in classes:
            print(cat['supercategory'])
            