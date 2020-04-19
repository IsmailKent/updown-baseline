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

filename = 'nocaps_val_vg_detector_features_adaptive.h5'    

class_label = int(input("enter class id to find average distance"))

with open('nocaps_val_detections.json','r') as oi_result, h5py.File(filename, 'r') as vg_result:
    results = json.load(oi_result)
    distances_same_label = []
    for a in results['annotations']:
        if a['category_id'] == class_label:
            look_for_box = a['bbox']
            in_image = a['image_id']
            boxes = np.array(vg_result['boxes'][in_image])
            boxes = boxes.reshape(boxes.size//4,4)
            print(look_for_box)
            print(boxes)