#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 15:28:13 2023

@author: cornelius
"""
import time
import math


start = time.time()
#calculate the modulus of an exponential
def modular_exponent(a,b,n):
    result = 1
    for i in range(0,b):
        result *= a
        result %= n
    
    return result

print(2**16+1)
print(modular_exponent(3, 65537, 341))

ende = time.time()
print(ende-start)
#print(bin(73))

start2 = time.time()
def fast_exponent(a,b,n):
    binary_list = []
    binary_string = str(bin(b))
    for i in range(2,len(binary_string)):
        binary_list.append(binary_string[i])

    binary_list.reverse()
    
    #print(binary_list)
    
    # calculate squares
    square_list = []
    square = a
    square_list.append(a)
    for i in range(0,len(binary_list)-1):
        square = (square**2)%n
        square_list.append(square)
    
    #print(square_list)
    
    # Multiply the squares
    product = 1
    binary_squares = list(zip(binary_list,square_list))
    #print(binary_squares)
    
    for element in binary_squares:
        if element[0]=='1':
            product *= element[1]%n
    
    return product%n
    
    
ende2 = time.time()
print(ende2-start2)
print(fast_exponent(3, 65537, 341))












