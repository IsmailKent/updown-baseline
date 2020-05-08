# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:02:10 2020

@author: Ismail
"""


import h5py

filename = '../data/coco_train2017_vg_detector_features_adaptive.h5'

with h5py.File(filename, 'r') as f:
    # List all groups
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]
