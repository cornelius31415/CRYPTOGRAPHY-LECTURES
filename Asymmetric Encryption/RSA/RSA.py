#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:20:05 2023

@author: cornelius
"""


import math

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
message = "i love you"


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


e = 2**16 +1 

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





#Here the actual encryption part starts

def encode(string):
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
    

#calculate the modulus of an exponential
def modular_exponent(a,b,n):
    result = 1
    for i in range(0,b):
        result *= a
        result %= n
    
    return result





#the actual RSA encryption
# public key (n,e)
def rsa_encrypt(x,pub): # x is a string
    n = pub[0]
    e = pub[1]
    encoded_message = encode(x)
    encrypted_message = []
    for i in range(0,len(encoded_message)):
        y = modular_exponent(encoded_message[i], e, n)
        encrypted_message.append(y)
    return encrypted_message

#the actual RSA deccryption
def rsa_decrypt(y,priv):
    n = priv[0]
    d = priv[1]
    decrypted_message = []
    for i in range(0,len(y)):
        x = modular_exponent(y[i], d, n)
        decrypted_message.append(x)
    plaintext = decode(decrypted_message)    
    return plaintext

    
secret = rsa_encrypt(message,pub)
print(secret)
plain = rsa_decrypt(secret,priv)
print(plain)



























pubkeylist = [(143,3),(391,3),(899,3)]
cipherlist = [60,203,711]

def rsa_hack(pubkeylist,cipherlist):
    e = pubkeylist[0][1]
    n_list = []
    n = 1
    for pub in pubkeylist:
        n_list.append(pub[0])
        n *= pub[0]
     
    N_list = []
    for element in n_list:
        N_list.append(n/element)
    
    y_list = []
    for i in range(0,len(n_list)):
        y_list.append(euklid_inverse(N_list[i], n_list[i]))
    
    factors = []
    for i in range(0,len(n_list)):
        factors.append(cipherlist[i]*y_list[i]*N_list[i])
    
    c = sum(factors)%n
   
    m = math.ceil(c**(1/e))  %n      
        
        
    return m
    
print(rsa_hack(pubkeylist,cipherlist))



#pub=(n,e)
def rsa_crack(pub1,pub2,pub3,c1,c2,c3):
    
    e = pub1[1]
    n1 = pub1[0]
    n2 = pub2[0]
    n3 = pub3[0]
    n = n1*n2*n3
      
    N1 = n/n1
    N2 = n/n2
    N3 = n/n3
    
    #calculate inverses
    y1 = euklid_inverse(N1,n1)
    y2 = euklid_inverse(N2,n2)
    y3 = euklid_inverse(N3,n3)
    
    
    c = (c1*y1*N1 + c2*y2*N2 + c3*y3*N3)%n
    
    m = math.ceil(c**(1/e))
    return m   
    
    

print(rsa_crack((143,3),(391,3),(899,3),60,203,711))




































