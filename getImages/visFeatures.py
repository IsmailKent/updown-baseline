# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:00:36 2020

@author: Ismail
"""

import h5py
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

filename = '../data/coco_val2017_vg_detector_features_adaptive.h5'
ID = int(input("enter image id to visualize"))
image = cv2.imread('im'+str(ID)+'.jpg')

with h5py.File(filename, 'r') as f:
    # List all groups
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]

    # Get the data
    data = list(f[a_group_key])
    index = 0
    # for i in range(4500):
    #     if (f['image_id'][i]==ID):
    #         index = i
            # break
    print (f['image_id'][index])
    boxes = np.array(f['boxes'][index])
    boxes = boxes.reshape(boxes.size//4,4)
    feat = np.array(f['features'][index])
    feat = feat.reshape(feat.size//2048,2048)
    print(boxes.shape)
    print (f['height'][index],f['width'][index],np.amax(boxes,axis=0))
    # print(feat.shape, boxes.shape)
    raise Exception()
    # print(boxes)
    fig,ax = plt.subplots(1)
    ax.imshow(image)
    
    cmap = plt.get_cmap('gnuplot')
    colors = [cmap(i) for i in np.linspace(0, 1, boxes.shape[0])]
    
    for i,box in enumerate(boxes):
    	#if f['features'][index][i]>=0.5:
	        # Create a Rectangle patch
	        rect = patches.Rectangle((box[0],box[1]),box[2]-box[0],box[3]-box[1],linewidth=1,edgecolor=colors[i],facecolor='none')
	        # Add the patch to the Axes
	        ax.add_patch(rect)
	        plt.text(box[0],box[1],'weight: '+str(f['features'][index][i]),color='red')
plt.savefig('features_im'+str(ID)+'_t.png')	
plt.show()
           