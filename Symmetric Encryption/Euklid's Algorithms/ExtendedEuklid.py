#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 11:40:00 2023

@author: cornelius
"""

#Extended Euklid Algorithm to calculate the multipicative Inverse 
# of a in Z_b
def euklid_inverse(a,b):

    a_list = []
    b_list = []
    rest = 1
    a_list.append(a)
    b_list.append(b)
    q_list = []
    
    while rest != 0:
        rest = a%b
        q = (a-rest)/b
        q_list.append(q)
        a = b
        b = rest
        a_list.append(a)
        b_list.append(b)
    
    # here starts the extended euclidean algorithm
    x = 0
    y = 1
    
    x_list = []
    y_list = []
    x_list.append(x)
    y_list.append(y)
    
    rev_q_list = list(reversed(q_list))

    

    for i in range(1,len(a_list)-1):
        x = y_list[i-1]
        x_list.append(x)
        y = x_list[i-1] - rev_q_list[i]*y_list[i-1]
        y_list.append(y)

    
    inverse = x_list[len(x_list)-1]%b_list[0]
    
    return inverse


print(euklid_inverse(11, 26))