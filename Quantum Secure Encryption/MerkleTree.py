#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 10:51:11 2024

@author: cornelius
"""



"""
---------------------------------- MERKLE TREE -----------------------------------------

                    1. Construct a Merkle Tree out of a data list
                    2. Determine the path of nodes in the Merkle Tree
                       from a leave to the root
                    3. Determine the authentication path from one leave
                       to the root
                    4. Authenticate the path of a leave


"""


import hashlib
import math


# -------------------- CONSTRUCT A MERKLE TREE ------------------------------------------


def tree(data):
    
    depth = int(math.log2(len(data)))     # depth of Merkle Tree
    
    hashed_leaves = [hashlib.sha256(str(i).encode()).hexdigest() for i in data]

    tree = []
    tree.append(hashed_leaves)

    for i in range(0,depth):
        num_nodes = 2**(depth-i) # Anzahl Knoten in einem Layer
        layer = []
        for k in range(0,num_nodes,2):
            node1 = ''.join(format(ord(i), '08b') for i in tree[i][k]) 
            node1 = [int(i) for i in node1]
            node2 = ''.join(format(ord(i), '08b') for i in tree[i][k+1]) 
            node2 = [int(i) for i in node2]
            
            
            node = [node1[i]+node2[i] for i in range(0,len(node1))]
            hash_node = hashlib.sha256(str(node).encode()).hexdigest()
            layer.append(hash_node)
        
            
        tree.append(layer)   
    
    
    return tree
    


# ------------------- DETERMINE THE PATH TO THE ROOT FROM ONE LEAVE ---------------------

"""

                    1. Choose a leave
                    2. Determine the index of the leave
                    3. If index is even, then it is the left neighbor
                       If index is odd, then it is the right neighbor
                    4. Determine the concatenated hash
                    5. Append hash to list of nodes leading to the root
                    5. Determine the index of the hash in this layer
                    6. Repeat everything until you reach the root

"""





def path(leave,merkle_tree):
    leave_idx = merkle_tree[0].index(leave)
    # path will be a list of nodes with the last node being the root hash
    path = []
    path.append(merkle_tree[0][leave_idx])
    leave_index = leave_idx  
    
    for layer_idx in range(0,len(merkle_tree)):
        layer = merkle_tree[layer_idx]
        if len(layer)>1 and leave_index %2 == 0:
            
            node1 = ''.join(format(ord(i), '08b') for i in layer[leave_index]) 
            node1 = [int(i) for i in node1]
            node2 = ''.join(format(ord(i), '08b') for i in layer[leave_index+1]) 
            node2 = [int(i) for i in node2]
            
        
            node = [node1[i]+node2[i] for i in range(0,len(node1))]
            hash_node = hashlib.sha256(str(node).encode()).hexdigest()
            path.append(hash_node)
            leave_index = merkle_tree[layer_idx+1].index(hash_node)
            
        elif len(layer)>1 and leave_index%2 !=0:
            
            node1 = ''.join(format(ord(i), '08b') for i in layer[leave_index]) 
            node1 = [int(i) for i in node1]
            node2 = ''.join(format(ord(i), '08b') for i in layer[leave_index-1]) 
            node2 = [int(i) for i in node2]
            
            node = node2 + node1
            hash_node = hashlib.sha256(str(node).encode()).hexdigest()
            path.append(hash_node)
            leave_index = merkle_tree[layer_idx+1].index(hash_node)
        
    return path




# ------------------- CREATE AUTHENTICATION PATH FOR A LEAVE ----------------------------

def authentication_path(leave, merkle_tree):
    
    leave_idx = merkle_tree[0].index(leave)
    
    path = []

    leave_index = leave_idx  
    
    for layer_idx in range(len(merkle_tree)):
        
        layer = merkle_tree[layer_idx]
        
        if len(layer)>1 and leave_index % 2 == 0:
            
            node1 = ''.join(format(ord(i), '08b') for i in layer[leave_index]) 
            node1 = [int(i) for i in node1]
            node2 = ''.join(format(ord(i), '08b') for i in layer[leave_index+1]) 
            node2 = [int(i) for i in node2]
            
         
            node = [node1[i]+node2[i] for i in range(0,len(node1))]
            hash_node = hashlib.sha256(str(node).encode()).hexdigest()
            path.append(layer[leave_index+1])
            leave_index = merkle_tree[layer_idx+1].index(hash_node)
            
        elif len(layer)>1 and leave_index % 2 !=0:
            
            node1 = ''.join(format(ord(i), '08b') for i in layer[leave_index]) 
            node1 = [int(i) for i in node1]
            node2 = ''.join(format(ord(i), '08b') for i in layer[leave_index-1]) 
            node2 = [int(i) for i in node2]
            

            node = [node1[i]+node2[i] for i in range(0,len(node1))]
            hash_node = hashlib.sha256(str(node).encode()).hexdigest()
            path.append(layer[leave_index-1])
            leave_index = merkle_tree[layer_idx+1].index(hash_node)
        
    
    
        
    return path


# -------------------- AUTHENTICATE A LEAVE ------------------------------------------

def authenticate_leave(leave,authentication_path,roothash):
        
    node1 = leave
    for element in authentication_path:
        node1 = ''.join(format(ord(i), '08b') for i in node1) 
        node1 = [int(i) for i in node1]
        node2 = ''.join(format(ord(i), '08b') for i in element)
        node2 = [int(i) for i in node2]
        node = [node1[i]+node2[i] for i in range(0,len(node1))]
        hash_node = hashlib.sha256(str(node).encode()).hexdigest()
        node1 = hash_node
    
    if node1 == roothash:
        return True
    else:
        return False
    
    
    pass


















































