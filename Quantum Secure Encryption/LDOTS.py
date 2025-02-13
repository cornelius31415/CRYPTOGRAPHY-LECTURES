#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 08:09:34 2024

@author: cornelius
"""










# ----------------------------------- LDOTS ------------------------------------------
"""
                        Lamport Diffie One Time Signature 
                    
                1. Turn a message string into a sequence of k bits
                
                
                2. Create a key with k rows and 2*k columns consisting
                   of random 0s and 1s (k is the security parameter)
                   
                   
                3. Create a Verification Key by hashing every element
                   of the key
                   
                   
                4. Create a signature for the message with the key. Every bit
                   of the message gets signed seperately. For every bit of the
                   message the column ( 2 * message_index + bit ) becomes part
                   of the signature.
                   
                   
                   
                   
                   
                   k = 2
                   message = 0 1
                   
                   signierschlüssel = ( 0 1 0 1        
                                        0 0 0 1)
                   
                   
                   signature =  (0 1
                                 0 1)
                   
                   
                   k = 3
                   message = 010
                   
                   signierschlüssel = (0 1 0 1 1 0       
                                       0 0 0 1 0 1
                                       1 0 1 0 1 0)
                   
                   signatur = (0 1 1
                               0 1 0
                               1 0 1)
                   
                   
                   
                5. Verify the signature of the message with the help of the
                   Verification Key. The corresponding columns have to match
                   the hashes of the columns of the signature.
            
                    k = 2
                    message = 01
                    
                    signierschlüssel = ( 0 1 0 1        
                                         0 0 0 1)
                    
                    verifikationsscl = ( h11 h12 h13 h14        
                                         h21 h22 h23 h24)
                    
                    
                    signature =  (0 1    
                                  0 1) 
                    
                    signature = (s11 s12    
                                 s21 s22 ) 

                  
                    Verifikation: h(s11) = h11 im Fall dass das erste Bit 0 ist
                                  h(s11) = h12 im Fall dass das erste Bit 1 ist
                        


                        k = 3
                        message = 010
                        
                        signierschlüssel = (0 1 0 1 1 0       
                                            0 0 0 1 0 1
                                            1 0 1 0 1 0)
                        
                        signatur = (0 1 1
                                    0 1 0
                                    1 0 1)
                        
                        verific = ( h11 h12 h13 h14 h15 h16
                                    h21 h22 h23 h24 h25 h26
                                    h31 h32 h33 h34 h35 h36)
                        
                        Verifikation: 
                        
                        




"""




















# ------------------------------------ IMPORTS --------------------------------

import numpy as np
import hashlib



# --------------------------------- KEY GENERATION ---------------------------



message = "1"


def signing_key(message):
    message = str(message)
    message =  ''.join(format(ord(i), '08b') for i in message)    
    message = [int(i) for i in message]  
    k = len(message) # Security Parameter
    return np.random.randint(0,2,size=(2*k,k)).tolist()

key = signing_key(message)
print(signing_key(message))
print()

def verification_key(key):
    
    verification_key = []
    
    for c in key:
        column = []
        for r in c:
            column.append(hashlib.sha256(str(r).encode()).hexdigest())
        
        verification_key.append(column)
        
    return verification_key





# ------------------------------- SIGNATURE ----------------------------------


def signature(message,key):
    
    message = str(message)
    message =  ''.join(format(ord(i), '08b') for i in message)    
    message = [int(i) for i in message] 
    
    signature = []
    for idx, bit in enumerate(message):
        signature.append(key[2*idx+bit])
    
    return signature
    
  

print(signature(message,key))

# ----------------------------- VERIFICATION ---------------------------------

"""

1. The Recipient receives (Message, Verfication Key, Signature, hash-function)
2. Recipient hashes each element of the Signature
3. Hashed Elements of the Signature get compared with the corresponding
    hashes in the Verification Key using the Message Bits as Reference

"""


def verification(message,verification_key,signature):
    
    message = str(message)
    message =  ''.join(format(ord(i), '08b') for i in message)    
    message = [int(i) for i in message] 
    
    hashed_signature = []
    
    if len(verification_key[0]) != len(message):
        return False
    
    else:
        for c in signature:
            column = []
            for r in c:
                column.append(hashlib.sha256(str(r).encode()).hexdigest())
        
            hashed_signature.append(column)

    
        for idx, bit in enumerate(message):
        
            if verification_key[2*idx+bit] != hashed_signature[idx]:
                return False
        
        return True
        
 




























