#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 15:25:27 2023

@author: cornelius
"""
print("\n")

import math
import hashlib
leaves = [1,2,3,4,5,6]

def tree_depth(blattanzahl):
    return int(math.log2(blattanzahl))
print(tree_depth(4))

def build_merkle_tree(leaves):
    # Merkle Tree only works, if number of leaves is power of 2
    # If len(leaves) even, append last 2 transactions until it is a power of 2
    # If len(leaves) odd, append last transaction until it is a power of 2
    
    if len(leaves)%2==0:
        while math.log2(len(leaves)).is_integer() is False:
            leaves.append(leaves[len(leaves)-2])
            leaves.append(leaves[len(leaves)-2])
    else:
        while math.log2(len(leaves)).is_integer() is False:
            leaves.append(leaves[-1])
        
    depth = tree_depth(len(leaves))
    hashed_leaves = \
        [hashlib.sha256(str(i).encode()).hexdigest() for i in leaves]
    
    tree = []
    tree.append(hashed_leaves)
    for i in range(0,depth):
        num_leaves = 2**(depth-i)
        new_leaves = []
        for k in range(0,num_leaves,2):
            node1 = hashed_leaves[k]
            node2 = hashed_leaves[k+1]
            new_node = \
                hashlib.sha256((str(node1)+str(node2)).encode()).hexdigest()
            new_leaves.append(new_node)
            
        hashed_leaves = new_leaves
        tree.append(new_leaves)
    return tree
    
merkle_tree = build_merkle_tree(leaves)
merkle_tree = list(reversed(merkle_tree))
for i in merkle_tree:
    print(i)
    print("\n")


