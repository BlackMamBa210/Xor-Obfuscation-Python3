#!/bin/python3
import os
import sys
import office2john
import binascii
import operator
import numpy as np
import bitstring
import subprocess
from bitstring import BitArray 
from arrays import obfuscation_array, InitialCode, XorMatrix, PadArray

# ascii_password = []


# def split(word): 
# 	return [char for char in word]

 

# def hash_password(hash):
#     password = bytearray(content[current_pos:(final_pos)], 'utf8')

#     for i in password:
#         x = binascii.unhexlify('%x' % i)
#         y = str(x).lstrip('b')
#         ascii_password.append(y.replace("'", ""))

#         password = ''.join(ascii_password)
        #print(password)



# FUNCTION CreatePasswordVerifier_Method1 PARAMETERS Password
def create_password_verifier(password):
    # SET Verifier TO 0x0000
    verifier = 0x0000
    # print(verifier)
    # SET PasswordArray TO (empty array of bytes)
    password_array = bytearray()
    # print(password_array)
    password_array.append(len(password))
    # print(password_array)
    password = binascii.unhexlify(password)
    password_array.extend(password)
    # print(type(password_array))
    print(password_array)
    password_array.reverse()
    # print(password_array)
    


    # FOR EACH PasswordByte IN PasswordArray IN REVERSE ORDER
    for password_byte in password_array:
        intermediate1 = 0
        print(password_byte)
        # IF (Verifier BITWISE AND 0x4000) is 0x0000
        if verifier & 0x4000 == 0x0000:
            intermediate1 = 0
            # SET Intermediate1 TO 0
        # ELSE
        else:
            # SET Intermediate1 TO 1
            intermediate1 = 1
        # ENDIF

        # SET Intermediate2 TO Verifier MULTIPLED BY 2
        intermediate2 = verifier * 2
        # SET most significant bit of Intermediate2 TO 0 #will come back to
        intermediate2 = setMSBto0(0)
        # SET Intermediate3 TO Intermediate1 BITWISE OR Intermediate2
        intermediate3 = intermediate1 ^ intermediate2
        # SET Verifier TO Intermediate3 BITWISE XOR PasswordByte
        verifier = intermediate3 ^ password_byte

        # ENDFOR

    # RETURN Verifier BITWISE XOR 0xCE4B
    return verifier ^ 0xCE4B


# END FUNCTION

# FUNCTION CreateXorArray_Method1
# PARAMETERS Password
# RETURNS array of 8-bit unsigned integers
# DECLARE XorKey AS 16-bit unsigned integer
# DECLARE ObfuscationArray AS array of 8-bit unsigned integers
def create_xor_array_method1(password):
    # SET XorKey TO CreateXorKey_Method1(Password)
    xor_key = create_xor_key_method1(password)
    # SET Index TO Password.Length
    index = len(password)
    temp_obfuscation_array = list(obfuscation_array)

    # IF Index MODULO 2 IS 1
    if index % 2 == 1:
        # SET Temp TO most significant byte of XorKey
        temp = findMsb(xor_key)  # set temp to msb of xor_key
        # SET ObfuscationArray[Index] TO XorRor(PadArray[0], Temp)
        temp_obfuscation_array[index] = xor_ror(list(PadArray)[0], temp)
        # DECREMENT Index
        index -= 1
        # SET Temp TO least significant byte of XorKey
        # temp = lsb of xor_key
        temp = findMsb(xor_key)
        # SET PasswordLastChar TO Password[Password.Length MINUS 1]
        password_last_char = password[len(password) - 1]
        # SET ObfuscationArray[Index] TO XorRor(PasswordLastChar, Temp)
        temp_obfuscation_array[index] = xor_ror(password_last_char, temp)

    # END IF
    # WHILE Index IS GREATER THAN to 0
    while index > 0:
        # DECREMENT Index
        index -= 1
        # SET Temp TO most significant byte of XorKey
        temp = findMsb(xor_key)
        byte_password_at_index = ord(password[index])
        # SET ObfuscationArray[Index] TO XorRor(Password[Index], Temp)
        temp_obfuscation_array[index] = xor_ror(byte_password_at_index, temp)

        # DECREMENT Index
        index -= 1
        # SET Temp TO least significant byte of XorKey
        temp = findLSB(xor_key)
        # SET ObfuscationArray[Index] TO XorRor(Password[Index], Temp)
        temp_obfuscation_array[index] = xor_ror(password[index], temp)

        # END WHILE
    # SET Index TO 15
    index == 15
    # SET PadIndex TO 15 MINUS Password.Length
    pad_index = 15 - len(password)
    # WHILE PadIndex IS greater than 0
    while pad_index > 0:
        # SET Temp TO most significant byte of XorKey
        temp = findMsb(xor_key)
        # SET ObfuscationArray[Index] TO XorRor(PadArray[PadIndex], Temp
        obfuscation_array[index] = xor_ror(PadArray[pad_index], temp)
        # DECREMENT Index
        index -= 1
        # DECREMENT PadIndex
        pad_index -= 1

        # SET Temp TO least significant byte of XorKey
        temp = findLSB(xor_key)
        # SET ObfuscationArray[Index] TO XorRor(PadArray[PadIndex], Temp)
        obfuscation_array[index] = xor_ror(PadArray[pad_index], temp)
        # DECREMENT Index
        index -= 1
        # DECREMENT PadIndex
        pad_index -= 1

    # END WHILE
    # RETURN ObfuscationArray
    return obfuscation_array


# FUNCTION CreateXorKey_Method1
# PARAMETERS Password
# RETURNS 16-bit unsigned integer
# DECLARE XorKey AS 16-bit unsigned integer
def create_xor_key_method1(password):
    # SET XorKey TO InitialCode[Password.Length MINUS 1]
    xor_key = list(InitialCode)[len(password) - 1] 

    # SET CurrentElement TO 0x00000068
    current_element = 0x00000068

    # FOR EACH Char IN Password IN REVERSE ORDER
    for char in password[::-1]:
        # FOR 7 iterations
        # IF (Char BITWISE AND 0x40) IS NOT 0
        if char and 0x40 != 0:
            # SET XorKey TO XorKey BITWISE XOR XorMatrix[CurrentElement]
            xor_key = xor_key | XorMatrix[current_element]
        # END IF
        else:
            # SET Char TO Char MULTIPLIED BY 2
            char = char * 2
            # DECREMENT CurrentElement
            current_element - 1
        return xor_key
    # END FOR

    # RETURN XorKey


# END FUNCTION

# FUNCTION XorRor
# PARAMETERS byte1, byte2
# RETURNS 8-bit unsigned integer
def xor_ror(byte1, byte2):
    # RETURN Ror(byte1 XOR byte2)
    if type(byte1) == int:
        pass
    else:
        byte1 = int(ord(byte1))
        
    if type(byte2) == int:
        pass
    else:
        byte2 = int(ord(byte2))
        
    byte3 = bin(byte1 ^ byte2)
    return byte3
    

# END FUNCTION

# FUNCTION Ror
# PARAMETERS byte
# RETURNS 8-bit unsigned integer
def ror(byte): #byte is not being manipulated
    # SET temp1 TO byte DIVIDED BY 2
    temp1 = int(byte) / 2
    # SET temp2 TO byte MULTIPLIED BY 128
    temp2 = byte * 128
    # SET temp3 TO temp1 BITWISE OR temp2
    temp3 = int(temp1) | int(temp2)
    
    # RETURN temp3 MODULO 0x100
    return temp3 % 0x100
    
# END FUNCTION

# def encrypt_data(password, data, XorArrayIndex):
data = bytearray(8)
# print(data)

XorArrayIndex = np.uint8(1)
unsigned_XorArrayIndex = XorArrayIndex + 2**32
# print(XorArrayIndex)

def encrypt_data(password, data, XorArrayIndex):
    # SET XorArray TO CreateXorArray_Method1(Password)
    xor_array = create_xor_array_method1(password)

    # FOR Index FROM 0 TO Data.Length
    for index in len(data):
        # SET Value TO Data[Index]
        value = data[index]
        # SET Value TO (Value rotate left 5 bits)
        value << 5
        # SET Value TO Value BITWISE XOR XorArray[XorArrayIndex]
        value = value ^ xor_array[XorArrayIndex]
        # SET DATA[Index] TO Value
        data[index] = value

        # INCREMENT XorArrayIndex
        XorArrayIndex += 1
        # SET XorArrayIndex TO XorArrayIndex MODULO 16
        XorArrayIndex = XorArrayIndex % 16
    # END FOR


# END FUNCTION

# FUNCTION DecryptData_Method1
# RPARAMETERS Password, Data, XorArrayIndex
def decrypt_data_method1(password, data, XorArrayIndex):
    # SET XorArray TO CreateXorArray_Method1(Password)
    xor_array = create_xor_array_method1(password)
    # FOR Index FROM 0 to Data.Length
    for index in data.length:
        # SET Value TO Data[Index]
        value = data[index]
        # SET Value TO (Value rotate right 5 bits)
        value >> 5
        # SET Data[Index] TO Value
        data[index] = value

        # INCREMENT XorArrayIndex
        XorArrayIndex += 1
        # SET XorArrayIndex TO XorArrayIndex MODULO 16
        XorArrayIndex = XorArrayIndex % 16
    # END FOR


# END FUNCTION


def findMsb(n):
    if n == 0:
        return 0

    msb = 0
    while n > 0:
        n = int(n / 2)
        msb += 1

    return 1 << msb


def findLSB(n):
    return n & -n


def setMSBto0(n):
    if n == 1:
        return 0
    result = lambda n: int("0" + bin(n)[3:], 2)
    return result(n)


if __name__ == "__main__":
    # password = os.system("python3 office2john.py test1.xls")
    # print(create_password_verifier(password).bit_length())
    # b = BitArray(bin = create_xor_array_method1("myPassword")[0])
    # print(int(b.uint).bit_length())
    excel_filename = sys.argv[1]
    # print(excel_filename)

    office2john_command = "python3 office2john.py {}".format(excel_filename)
    # print(office2john_command)

    hash_verifier = os.system(office2john_command)
    # print(hash_verifier)

    direct_output = str(subprocess.check_output(office2john_command, shell=True)).split('*')[-3:]
    # print(direct_output)
    # print(direct_output[0])
    hash_verifier = ''.join(direct_output).split(":")[0]
    # print('DEBUG: hash_verifier =' + ' ' + hash_verifier)
    # ascii_password = split(direct_output[0])
    # for i in ascii_password:
    #     hash_password(i)
    create_password_verifier(hash_verifier)
    print(create_password_verifier)

    # create_xor_array_method1(hash_verifier[0])
    # print(create_xor_array_method1)

    # create_xor_key_method1(hash_verifier[0])
    # print(create_xor_key_method1)

    # xor_ror(hash_verifier[0], hash_verifier[1])
    # print(xor_ror)

    # ror(hash_verifier[0])
    # print(ror)

    # encrypt_data(hash_verifier[0], data, XorArrayIndex)
    # print(encrypt_data)