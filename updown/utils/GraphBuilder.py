# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:13:58 2020
@author: Ismail
"""
import torch 
import numpy as np
from scipy.linalg import block_diag

"""
Loops: Whenever you think you need a loop stop and think. Most of the time you do not and in fact do not even want one. It is much faster both to write and run code without loops.
Memory allocation: Whenever you know the size of an object, preallocate space for it. Growing memory, particularly in Python lists, is very slow compared to the alternatives.
"""


                      
    
    
def get_adj_mat(image_boxes:  torch.FloatTensor):                                                                                                                                                                                          N = image_boxes.shape[0]
    return torch.ones((N,N)).cuda()
"""
    center = torch.zeros(image_boxes.shape[0],2).type_as(image_boxes)
    center[:,0] = (image_boxes[:,2]-image_boxes[:,0])/2 + image_boxes[:,0]
    center[:,1] = (image_boxes[:,3]-image_boxes[:,1])/2 + image_boxes[:,1]
    x2 = torch.square(center).sum(-1).view(N,1).repeat(1,N).cuda() # shape is (N,N)
    y2 = torch.square(center).sum(-1).view(1,N).repeat(N,1).cuda() # shape is (N,N)
    xy = torch.mm(center,center.t()).cuda() # shape is (N,N)
    dists = torch.sqrt(x2 + y2 - 2*xy) + torch.ones((N,N)).cuda() # shape is (N, N)
    A = 1/torch.square(dists)
    A[torch.isnan(A)]=0
    if (torch.isnan(A).any()):
        print("NAN")
    return A
<<<<<<< HEAD
    """   
=======
"""
>>>>>>> f3dcbf030646f05f0f9f8aea50bc17baebc86713
          
            
def build_batch_graph(batch_features:  torch.FloatTensor, batch_boxes:  torch.FloatTensor) -> (torch.FloatTensor , torch.FloatTensor):
    adj_matrices = torch.FloatTensor(batch_boxes.shape[0],batch_boxes.shape[1],batch_boxes.shape[1])
    for idx in range(batch_boxes.shape[0]):
        boxes = batch_boxes[idx]
        A = get_adj_mat(boxes)
        adj_matrices[idx] = A.squeeze()
    batch_adj_Matrix = torch.from_numpy(block_diag(*adj_matrices))
    batch_features = list(batch_features)
    batch_features = torch.cat(batch_features)
    batch_feature_Matrix = torch.stack(list(batch_features))
    return batch_adj_Matrix, batch_feature_Matrix
    
 
            
