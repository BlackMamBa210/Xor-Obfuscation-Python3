#!/bin/python3
import os
import sys
import office2john
import bitstring
import operator
import numpy as np


from arrays import obfuscation_array, InitialCode, XorMatrix, PadArray

password = list(
    bytes(
        b"7e0da6b9673ca827556506d7332df0b25cd62504d3e94e265f445ce9285bb85b7384933c14128384c8c9a770688fba6c"
    )
)

# FUNCTION CreatePasswordVerifier_Method1 PARAMETERS Password
def create_password_verifier(password):
    # SET Verifier TO 0x0000
    verifier = 0x0000

    # SET PasswordArray TO (empty array of bytes)
    password_array = bytearray()

    password_array.append(len(password))
    password_array.(password)

    # FOR EACH PasswordByte IN PasswordArray IN REVERSE ORDER
    for password_byte in reversed(password_array):
        intermediate1 = 0

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
        temp = xor_key.findLSB(xor_key)
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
    xor_key = list(InitialCode)[len(password) - 1]  # cant get rid of this error

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
    return ror(byte1 ^ byte2)


# END FUNCTION

# FUNCTION Ror
# PARAMETERS byte
# RETURNS 8-bit unsigned integer
def ror(byte):
    # SET temp1 TO byte DIVIDED BY 2
    temp1 = byte / 2
    # SET temp2 TO byte MULTIPLIED BY 128
    temp2 = byte * 128
    # SET temp3 TO temp1 BITWISE OR temp2
    temp3 = temp1 | temp2
    # RETURN temp3 MODULO 0x100
    return temp3 % 0x100


# END FUNCTION

# def encrypt_data(password, data, XorArrayIndex):
def encrypt_data(password, data, XorArrayIndex):
    # SET XorArray TO CreateXorArray_Method1(Password)
    xor_array = create_xor_array_method1(password)

    # FOR Index FROM 0 TO Data.Length
    for index in data.length:
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
    # password = os.system("python3 office2john.py easypasswd.xlsx")
    # print(create_password_verifier(password).bit_length())
    print(create_xor_array_method1("myPassword")[0].bit_length())

