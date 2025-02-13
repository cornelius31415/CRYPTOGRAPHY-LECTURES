#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 17:05:17 2023

@author: cornelius
"""

alphabet = ["a","b","c","d","e","f","g","h","i","j","k",
            "l","m","n","o","p","q","r","s","t","u","v",
            "w","x","y","z"]

# Wandelt String in Liste von Zahlen um. Jede Zahl
# entspricht der Position des Buchstabens im Alphabet
def encode(string):
    number_list = []
    for i in range (0,len(string)):
        for j in range(0,len(alphabet)):
            if string[i] == alphabet[j]:
                number_list.append(j)
    return number_list 

print(encode("hello"))

# Wandelt eine Liste von Zahlen in einen Text um.
# Gegenstück zu encode()
def decode(number_list):
    string = ""
    for i in range(0,len(number_list)):
        string += alphabet[number_list[i]]
    return string

print(decode([7, 4, 11, 11, 14]))

def encrypt(message, key):
    
    message = str(message) # Zur Sicherheit in String umwandeln
    message = message.lower() # In Lowercase umwandeln
    message = encode(message) # als Liste von Zahlen ausgeben
    secret = []
    for letter in message:
        new_letter = letter+key
        secret.append(new_letter)
    return decode(secret)
 
print(encrypt("hallo",1))    
    
def decrypt(secret,key):
    secret = str(secret)
    secret = secret.lower()
    secret = encode(secret)
    plain = []
    for letter in secret:
        new_letter = letter-key
        plain.append(new_letter)
    return decode(plain)
      
print(decrypt('ibmmp',1))








    









