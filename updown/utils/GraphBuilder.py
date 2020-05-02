# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:13:58 2020

@author: Ismail
"""
import torch 
import numpy as np
from scipy.linalg import block_diag


def calc_distance(box1, box2):
    #print("here fine 11")
    mid_point_1 = torch.Tensor([ box1[2] - box1[0] , box1[3]- box1[1]])
    mid_point_2 = torch.Tensor([ box2[2] - box2[0] , box2[3] - box2[1]])
    #print("here fine 12")
    return  np.linalg.norm (mid_point_1 - mid_point_2)


def get_adj_mat(image_boxes:  torch.FloatTensor):
    n_nodes = image_boxes.shape[0]
    A = torch.eye(n_nodes)
    
    for idx1, box1 in enumerate(image_boxes):
        for idx2 in range(idx1,image_boxes.shape[0]):
            if idx1==idx2:
                continue
            box2 = image_boxes[idx2]
            dist = calc_distance(box1,box2)
            weight= np.exp(-dist/100)
            A[idx1][idx2] = weight
            A[idx2][idx1]= weight
    return torch.FloatTensor(A)
          
            
def build_batch_graph(batch_features:  torch.FloatTensor, batch_boxes:  torch.FloatTensor):
    adj_matrices = []
    for idx in range(batch_boxes.shape[0]):
        boxes = batch_boxes[idx]
        A = get_adj_mat(boxes)
        adj_matrices.append(A)
    batch_adj_Matrix = block_diag(*adj_matrices)
    batch_features = batch_features.cpu()
    batch_features = list(batch_features)
    batch_features = torch.cat(batch_features)
    batch_feature_Matrix = torch.stack(list(batch_features))
    
    
    return torch.FloatTensor(batch_adj_Matrix), torch.FloatTensor(batch_feature_Matrix)
    
 
            