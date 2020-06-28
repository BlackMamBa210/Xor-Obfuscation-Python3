#!/bin/python3
import os
import sys
import office2john
import bitstring
import numpy as np

from arrays import obfuscation_array, InitialCode, XorMatrix, PadArray

password = "testpassword"


def create_password_verifier(password):
    verifier = b"0x0000"

    password_array = bitstring.BitArray([])
    password_array[0] = len(password_array)
    password_array.append(password)

    for password_byte in reversed(password_array):
        intermediate1 = 0

        if verifier & b"0x4000" != b"0x0000":
            intermediate1 = 1

        intermediate2 = verifier * 2
        intermediate2 = (verifier * 2) & 0x7FFF
        intermediate2 = 0
        intermediate3 = intermediate1 ^ intermediate2
        verifier = intermediate3 ^ 0xCE4B
        break
    return verifier ^ 0xCE4B


def create_xor_array_method1(password):
    xor_key = create_xor_key_method1(
        password
    )  # this one doesnt make too much sense #SET XorKey TO CreateXorKey_Method1(Password
    index = password.length  # questionable line
    temp_obfuscation_array = list(obfuscation_array)

    if index % 2 == 1:
        temp = 0x7FFF  # set temp to msb of xor_key
        temp_obfuscation_array[index] = xor_ror(
            list(PadArray)[0], temp
        )  # I do not know how to set this one #SET ObfuscationArray[Index] TO XorRor(PadArray[0], Temp)
        index -= 1
        # temp = lsb of xor_key
        password_last_char = password[len(password) - 1]
        temp_obfuscation_array[index] = xor_ror(password_last_char, temp)

    while index > 0:
        index -= 1

    obfuscation_array[index] = xor_ror(password[index], temp)

    while index == 15:
        pad_index = 15 - len(password)

    while pad_index > 0:
        #SET Temp TO most significant byte of XorKey
        obfuscation_array[index] = xor_ror(PadArray[pad_index], temp)
        index -= 1
        pad_index -= 1

    #SET Temp TO least significant byte of XorKey
    obfuscation_array[index] = xor_ror(PadArray[pad_index], temp)
    index -= 1
    pad_index -= 1

    #these two lines dont make much sense. While what?
    #END WHILE
        #RETURN ObfuscationArray

def create_xor_key_method1(password):
    xor_keys = list(InitialCode(len(password) - 1)) #cant get rid of this errorr

    current_element = 0x00000068

    for char in password[::-1]:
        if char and 0x40 != 0:
            xor_keys = xor_key | XorMatrix
        else:
            char = char * 2
            current_element - 1
    return xor_keys


def xor_ror(byte1, byte2):
    return ror(byte1 ^ byte2)


def ror(byte):
    temp1 = byte / 2
    temp2 = byte * 128
    temp3 = temp1 | temp2
    return temp3 % 0x100


# def encrypt_data(password, data, XorArrayIndex):

# for index in data.length:


def setBitNumber(n):
    if n == 0:
        return 0

    msb = 0
    while n > 0:
        n = int(n / 2)
        msb += 1

    return 1 << msb


if __name__ == "__main__":
    password = os.system("python3 office2john.py easypasswd.xlsx")
    print(password_verifier)
    password_verifier("testpassword")
