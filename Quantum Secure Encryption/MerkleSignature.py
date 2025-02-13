#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:16:50 2024

@author: cornelius
"""

"""
----------------------------- MERKLE SIGNATURE SCHEME -------------------------------



                1. Declare the size of parameter H
                2. Create  a list of 2**H  LDOTS- Signing - Keys
                3. Create the corresponding Verification Key list
                4. Create a Merkle Tree of the Verification Keys
                5. The private key is the sequence of One-Time Signing Keys
                   The public key is the root of the Merkle Tree
                6. The signature contains the following information:
                   - the public key (root hash)
                   - the verification key
                   - the One-Time-Signature
                   - the authentication path 
                7. The recipient receives the Signature, The Public Key and the Message
                8. Verification Process:
                   - The One-Time Signature gets verified with the
                     Verification Key
                   - With the authentication path one checks if the 
                     Verification Key leads to the same root hash (public key)
                   
                 
"""


import LDOTS as ld
import MerkleTree as mt
import hashlib

message = "h"

def key_generation(H,message):
    
    key_amount = 2 ** H
    private_key = [ld.signing_key(message) for i in range(0,key_amount)]
    verification_keys = [ld.verification_key(key) for key in private_key]
    merkle_tree = mt.tree(verification_keys)
    public_key = merkle_tree[-1][0]  
               # public key = root hash
    return (public_key, private_key,merkle_tree,verification_keys)




def signature(message,public_key,private_key,merkle_tree,verification_key):
    
    """
    The signature contains the following information:
       - the public key (root hash)
       - the verification key
         the Merkle Tree
       - the One-Time-Signature
       - the authentication path 
    """
    
    
    verification_hash = hashlib.sha256(str(verification_key).encode()).hexdigest()
    authentication_path = mt.authentication_path(verification_hash, merkle_tree)
    onetime_signature = ld.signature(message, private_key)
    
    return (public_key, verification_key, onetime_signature, authentication_path )




def verify(message, signature):
    
    """
    Signature = (public_key, verification_key, index of verification_key in merkle tree,
                 One-Time-Signature, Authentication path)
    1. Check if One-Time-Signature is correct
    2. Hash the verification key
    3. Check if by applying the authentication path one arrives at the public key
    """
    
    public_key = signature[0]
    verification_key = signature[1]
    onetime_signature = signature[2]
    authentication_path = signature[3]
    
    verify_ots = ld.verification(message, verification_key, onetime_signature)
    
    if verify_ots == True:
        verification_hash = hashlib.sha256(str(verification_key).encode()).hexdigest()
        authenticate = mt.authenticate_leave(verification_hash, authentication_path, public_key)
        return authenticate
    
    else:
        return False
    
































