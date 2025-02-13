#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 14:00:15 2023

@author: cornelius
"""

import math

#Advanced Euklid Algorithm to calculate the multipicative Inverse of the public key
#Used to calcualte the private key
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
        pass
    
    inverse = x_list[len(x_list)-1]%b_list[0]
    
    return inverse

def publicKeyGeneration(p,q):
    n = p*q
    m = (p-1)*(q-1)
    e = 0
    for i in range(25,m):
        if math.gcd(i,m)==1:
            e = i
            break
    pub = (n,e)    
    return pub

def privateKeyGeneration(p,q,pub):
    e = pub[1]
    m = (p-1)*(q-1)
    d = euklid_inverse(e,m)
    priv = (pub[0],int(d))
    return priv


pub = publicKeyGeneration(31, 37)
priv = privateKeyGeneration(31, 37, pub)
print(pub)
print(priv)