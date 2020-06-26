#!/bin/python3
import os
import sys

import numpy as np

import office2john
import bitstring


password = b'testpassword'

def password_verifier(password):
    verifier = np.uint16(1)
    password_array = np.uint8(1)
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
        
        
PadArray = [ 0xBB, 
             0xFF, 
             0xFF, 
             0xBA, 
             0xFF, 
             0xFF, 
             0xB9, 
             0x80, 
             0x00, 
             0xBE, 
             0x0F, 
             0x00, 
             0xBF, 
             0x0F, 
             0x00
            ]

InitialCode = [ 0xE1F0, 
                0x1D0F, 
                0xCC9C, 
                0x84C0, 
                0x110C, 
                0x0E10, 
                0xF1CE, 
                0x313E, 
                0x1872, 
                0xE139, 
                0xD40F, 
                0x84F9,
                0x280C, 
                0xA96A, 
                0x4EC3
                ]

XorMatrix = [ 0xAEFC, 
              0x4DD9,
              0x9BB2, 
              0x2745, 
              0x4E8A, 
              0x9D14, 
              0x2A09, 
              0x7B61, 
              0xF6C2, 
              0xFDA5, 
              0xEB6B, 
              0xC6F7, 
              0x9DCF, 
              0x2BBF, 
              0x4563, 
              0x8AC6, 
              0x05AD, 
              0x0B5A, 
              0x16B4, 
              0x2D68, 
              0x5AD0, 
              0x0375, 
              0x06EA, 
              0x0DD4, 
              0x1BA8, 
              0x3750, 
              0x6EA0, 
              0xDD40, 
              0xD849, 
              0xA0B3, 
              0x5147, 
              0xA28E, 
              0x553D, 
              0xAA7A, 
              0x44D5, 
              0x6F45,
              0xDE8A, 
              0xAD35, 
              0x4A4B, 
              0x9496, 
              0x390D, 
              0x721A, 
              0xEB23, 
              0xC667, 
              0x9CEF, 
              0x29FF, 
              0x53FE, 
              0xA7FC, 
              0x5FD9, 
              0x47D3, 
              0x8FA6, 
              0x0F6D, 
              0x1EDA, 
              0x3DB4, 
              0x7B68, 
              0xF6D0, 
              0xB861, 
              0x60E3, 
              0xC1C6, 
              0x93AD, 
              0x377B, 
              0x6EF6, 
              0xDDEC, 
              0x45A0, 
              0x8B40, 
              0x06A1, 
              0x0D42, 
              0x1A84, 
              0x3508, 
              0x6A10,
              0xAA51, 
              0x4483, 
              0x8906, 
              0x022D, 
              0x045A, 
              0x08B4, 
              0x1168, 
              0x76B4, 
              0xED68, 
              0xCAF1, 
              0x85C3, 
              0x1BA7, 
              0x374E, 
              0x6E9C, 
              0x3730, 
              0x6E60, 
              0xDCC0, 
              0xA9A1, 
              0x4363, 
              0x86C6, 
              0x1DAD, 
              0x3331, 
              0x6662, 
              0xCCC4, 
              0x89A9, 
              0x0373, 
              0x06E6, 
              0x0DCC, 
              0x1021, 
              0x2042, 
              0x4084, 
              0x8108, 
              0x1231, 
              0x2462, 
              0x48C4
            ]

def create_xor_array(password):
    xor_key = np.uint16(1)
    obfuscation_array = np.unit8(1)

    xor_key = xor_array
    index = password.length #questionable line
    obfuscation_array = (0x00, 
                         0x00, 
                         0x00, 
                         0x00, 
                         0x00, 
                         0x00, 
                         0x00, 
                         0x00,
                         0x00, 
                         0x00, 
                         0x00, 
                         0x00, 
                         0x00, 
                         0x00, 
                         0x00, 
                         0x00
                         )

    if index % 1:
        temp = 0x7fff

    if index % 2 == 1:
        temp = 0x7fff
        obfuscation_array = PadArray

    index = index - 1

def xor_key(password):
    xor_keys = np.unit16(1)
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

def encrypt_data(password, data, XorArrayIndex):
    xor_array = np.unit8(1)
    
    for index in data.length:
        
    
            
    

    

if __name__ == "__main__":
    #password = os.system("python3 office2john.py easypasswd.xlsx")
    #print(password_verifier)
    password_verifier("testpassword")
    print(encrypt_data)