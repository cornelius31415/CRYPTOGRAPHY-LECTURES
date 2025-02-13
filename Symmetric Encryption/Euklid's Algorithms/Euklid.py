#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 11:39:32 2023

@author: cornelius
"""


#Euklid Algorithm to calculate the biggest common divisor 
#Used to calcualte the public key
def euklid(a,b):
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
    
    ggT = b_list[len(b_list)-2]
    return ggT

print(euklid(950,41))


