#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:24:23 2023

@author: cornelius
"""
import math
from egcd import egcd

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
            "n","o","p","q","r","s","t","u","v","w","x","y","z"]


def encode(string):
    string = string.lower()
    number_list = []
    for i in range (0,len(string)):
        for j in range(0,len(alphabet)):
            if string[i] == alphabet[j]:
                number_list.append(j)
    return number_list           
                

def decode(number_list):
    string = ""
    for i in range(0,len(number_list)):
        string += alphabet[number_list[i]]
    return string



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

print(euklid(4,26))
print(math.gcd(4,26))






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
print(egcd(11,26))


    




print("Encoding")

# key = (a,b)
def Enc(key,plaintext):
    m = len(alphabet)
    a = key[0]
    b = key[1]
    plaintext = encode(plaintext)
    cipher = []
    for letter in plaintext:
        cipher.append((a*letter+b)%m)
    cipher_dec = decode(cipher)
    return plaintext, cipher_dec, cipher
    
print(Enc((7,3), "Hallo"))




# key = (a,b)
def Dec(key,text):
    m = len(alphabet)
    a = euklid_inverse(key[0],m)
    b = key[1]
    text = encode(text)
    cipher = []
    for letter in text:
        cipher.append(int((a*(letter-b))%m))
    cipher_dec = decode(cipher)
    return text, cipher_dec, cipher



print(Dec((7,3),'adccx'))





























