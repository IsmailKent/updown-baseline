# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:13:58 2020

@author: Ismail
"""
import torch 
import numpy as np
from scipy.linalg import block_diag
import math

"""
Loops: Whenever you think you need a loop stop and think. Most of the time you do not and in fact do not even want one. It is much faster both to write and run code without loops.
Memory allocation: Whenever you know the size of an object, preallocate space for it. Growing memory, particularly in Python lists, is very slow compared to the alternatives.
"""


def calc_distance(box1, box2):
    mid_point_1 = torch.Tensor([box1[0],box1[1]]) + torch.Tensor([ box1[2] - box1[0] , box1[3]- box1[1]])
    mid_point_2 = torch.Tensor([box2[0],box2[1]]) + torch.Tensor([ box2[2] - box2[0] , box2[3] - box2[1]])
    return  math.sqrt( (mid_point_1[0]-mid_point_2[0])**2 + (mid_point_1[1]-mid_point_2[1])**2)


def get_adj_mat(image_boxes:  torch.FloatTensor):
    n_nodes = image_boxes.shape[0]
    A = torch.eye(n_nodes)
    
    for idx1, box1 in enumerate(image_boxes):
        for idx2 in range(idx1+1,image_boxes.shape[0]):
            box2 = image_boxes[idx2]
            dist = calc_distance(box1,box2)
            A[idx1][idx2] = dist
            A[idx2][idx1]= dist
    A = torch.exp(-A/500)    
    return A
          
            
def build_batch_graph(batch_features:  torch.FloatTensor, batch_boxes:  torch.FloatTensor):
    adj_matrices = torch.FloatTensor(batch_boxes.shape[0],batch_boxes.shape[1],batch_boxes.shape[1])
    for idx in range(batch_boxes.shape[0]):
        boxes = batch_boxes[idx]
        A = get_adj_mat(boxes)
        adj_matrices[idx] = A.squeeze()
    print("1")
    batch_adj_Matrix = torch.from_numpy(block_diag(*adj_matrices))
    batch_features = list(batch_features)
    batch_features = torch.cat(batch_features)
    batch_feature_Matrix = torch.stack(list(batch_features))
    print(type(batch_adj_Matrix))
    print("2")
    return torch.from_numpy(batch_adj_Matrix), torch.FloatTensor(batch_feature_Matrix)
    
 
            