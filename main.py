#!/bin/python3
import os
import sys
import office2john
import bitstring
import numpy as np

import arrays


password = b'testpassword'

def password_verifier(password):
    verifier = 0x0000
    
    password_array = bitstring.BitArray([])
    password_array.append(len(password))         

    for byte in password_array[::-1]:

        intermediate1 = 0

        if verifier & 0x4000 == 0x0000:
            intermediate1 = 0
        else:
            intermediate1 = 1

            
        intermediate2a = bitstring.BitArray(verifier * 2)
        intermediate2 = (verifier * 2) & 0x7fff
        intermediate2 = 0
        intermediate3 = intermediate1 ^ intermediate2
        verifier = intermediate3 ^ 0xCE4B
        break
    return verifier ^ 0xCE4B

def create_xor_array(password):
    xor_key = xor_array #this one doesnt make too much sense #SET XorKey TO CreateXorKey_Method1(Password
    index = password.length #questionable line


    if index % 1:
        temp = 0x7fff

    if index % 2 == 1:
        temp = 0x7fff
        obfuscation_array = PadArray #I do not know how to set this one #SET ObfuscationArray[Index] TO XorRor(PadArray[0], Temp)

    index = index - 1

def xor_key(password):
    xor_keys = InitialCode(len(password) - 1)
    
    current_element = 0x00000068

    for char in password[::-1]:
        if char and 0x40 != 0:
            xor_keys =  xor_key | XorMatrix
        else:
            char = char * 2
            current_element - 1
    return xor_keys

def xor_ror(byte1, byte2):
    return ror(byte1 ^ byte2)

def ror(byte):
    temp1 = byte / 2
    temp2 = byte * 128
    temp3 - temp1 | temp2
    return temp3 % 0x100

#def encrypt_data(password, data, XorArrayIndex):
    
    #for index in data.length:
        
    
            
    

    

if __name__ == "__main__":
    #password = os.system("python3 office2john.py easypasswd.xlsx")
    #print(password_verifier)
    password_verifier("testpassword")
    print(password_verifier)
    print(create_xor_array)
    print(xor_key)
    print(xor_ror)
    print(ror)
