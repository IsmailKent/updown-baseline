# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:15:29 2020

@author: Ismail
"""

"""
Steps:
    1- get class_label
    2- look for boxes with this class label
    3- get image_id of this box
    4- open this image, look for this box, get its feature
    5- calculated L2 distance, add to list of distances
"""


import json
import h5py
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

filename = '../data/nocaps_val_vg_detector_features_adaptive.h5'    

class_label = int(input("enter class id to find average distance:  "))

with open('nocaps_val_detections.json','r') as oi_result, h5py.File(filename, 'r') as vg_result:
    results = json.load(oi_result)
    distances_same_label = []
    for a in results['annotations']:
        if a['category_id'] == class_label:
            look_for_box = a['bbox']
            print("look_for_box: ",look_for_box)
            in_image = a['image_id']
            print("in_image: ",in_image)
            index = 0
            for i in range(4500):
                if (vg_result['image_id'][i]==in_image):
                    index = i
                    break
            print(vg_result['image_id'][index])
            boxes = np.array(vg_result['boxes'][index])
            boxes = boxes.reshape(boxes.size//4,4)
            print("first box in boxes:  ", list(boxes[0]))
            print(boxes)
            index_closest_box = 0
            min_distance = 99999
            for i, box in enumerate(boxes):
                x1,y1,x2,y2 = tuple(box)
                lx1,ly1,lx2,ly2 = tuple(look_for_box)
                distance = np.sqrt((x1-lx1)**2 + (y1-ly1)**2) + np.sqrt((x2-lx2)**2+(y2-ly2)**2)
                if distance<min_distance:
                    min_distance = distance
                    index_closest_box=i
            print(boxes[index_closest_box])
            break
