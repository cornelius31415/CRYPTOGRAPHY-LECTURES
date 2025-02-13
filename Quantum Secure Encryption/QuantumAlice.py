#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 10:39:37 2024

@author: cornelius
"""

"""
                        QUANTUM ALICE
            
            Alice wants to send a message m to Bob
            She also wants to prove that it was her who sent the message
            So she sends along a signature
            Each One Time Signature can only be used once
            so as long as the programm is running and one is typing in
            messages, new keys are getting picked out



"""

import LDOTS as ld 
import MerkleTree as mt
import MerkleSignature as ms
import hashlib

# -------------------------- Lamport Diffie One Time Signature --------------------------------


message = "hello"
signing_key = ld.signing_key(message)
verify_key = ld.verification_key(signing_key)
signature = ld.signature(message, signing_key)
verify_signature = ld.verification("h", verify_key, signature)

"""
print(signing_key)
print()
print(verify_key)
print()
print(signature)
print()
print(verify_signature)
print()

"""
# -------------------------- MERKLE TREE -------------------------------------------

data = [1,2,3,4]
tree = mt.tree(data)
leave = tree[0][0]
path = mt.path(leave,tree)
authentication_path = mt.authentication_path(leave, tree)
authenticate = mt.authenticate_leave(leave, authentication_path, tree[-1][0])

"""
print(tree)
print()
print(leave)
print()
print(path)
print()
print(authentication_path)
print()
print(authenticate)
"""

# ------------------------ MERKLE SIGNATURE ----------------------------------------



public_key, private_key, merkle_tree, verification_keys = ms.key_generation(3, message)

verification_key = verification_keys[0]

signature = ms.signature(message, public_key, private_key[0], merkle_tree, verification_key)

print(signature)
print()

verify = ms.verify("hello", signature)
print(verify)































