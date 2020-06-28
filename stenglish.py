# FUNCTION CreatePasswordVerifier_Method1 PARAMETERS Password
# RETURNS 16-bit unsigned integer
# DECLARE Verifier AS 16-bit unsigned integer
# DECLARE PasswordArray AS array of 8-bit unsigned integers
# SET Verifier TO 0x0000
# SET PasswordArray TO (empty array of bytes) SET PasswordArray[0] TO Password.Length APPEND Password TO PasswordArray
# FOR EACH PasswordByte IN PasswordArray IN REVERSE ORDER IF (Verifier BITWISE AND 0x4000) is 0x0000
#           SET Intermediate1 TO 0
#        ELSE
#           SET Intermediate1 TO 1
#        ENDIF
# SET Intermediate2 TO Verifier MULTIPLED BY 2 SET most significant bit of Intermediate2 TO 0
# SET Intermediate3 TO Intermediate1 BITWISE OR Intermediate2
# SET Verifier TO Intermediate3 BITWISE XOR PasswordByte ENDFOR
#     RETURN Verifier BITWISE XOR 0xCE4B
# END FUNCTION



# SET PadArray TO ( 0xBB, 0xFF, 0xFF, 0xBA, 0xFF, 0xFF, 0xB9, 0x80, 0x00, 0xBE, 0x0F, 0x00, 0xBF, 0x0F, 0x00 )
# SET InitialCode TO
# SET XorMatrix TO (
# ( 0xE1F0, 0x1D0F, 0xCC9C, 0x84C0, 0x110C, 0x0E10, 0xF1CE, 0x313E, 0x1872, 0xE139, 0xD40F, 0x84F9, 0x280C, 0xA96A, 0x4EC3 )
# 0xAEFC, 0x4DD9, 0x9BB2, 0x2745, 0x4E8A, 0x9D14, 0x2A09, 0x7B61, 0xF6C2, 0xFDA5, 0xEB6B, 0xC6F7, 0x9DCF, 0x2BBF, 0x4563, 0x8AC6, 0x05AD, 0x0B5A, 0x16B4, 0x2D68, 0x5AD0, 0x0375, 0x06EA, 0x0DD4, 0x1BA8, 0x3750, 0x6EA0, 0xDD40, 0xD849, 0xA0B3, 0x5147, 0xA28E, 0x553D, 0xAA7A, 0x44D5, 0x6F45, 0xDE8A, 0xAD35, 0x4A4B, 0x9496, 0x390D, 0x721A, 0xEB23, 0xC667, 0x9CEF, 0x29FF, 0x53FE, 0xA7FC, 0x5FD9, 0x47D3, 0x8FA6, 0x0F6D, 0x1EDA, 0x3DB4, 0x7B68, 0xF6D0, 0xB861, 0x60E3, 0xC1C6, 0x93AD, 0x377B, 0x6EF6, 0xDDEC, 0x45A0, 0x8B40, 0x06A1, 0x0D42, 0x1A84, 0x3508, 0x6A10,
# 0xAA51, 0x4483, 0x8906, 0x022D, 0x045A, 0x08B4, 0x1168, 0x76B4, 0xED68, 0xCAF1, 0x85C3, 0x1BA7, 0x374E, 0x6E9C, 0x3730, 0x6E60, 0xDCC0, 0xA9A1, 0x4363, 0x86C6, 0x1DAD, 0x3331, 0x6662, 0xCCC4, 0x89A9, 0x0373, 0x06E6, 0x0DCC, 0x1021, 0x2042, 0x4084, 0x8108, 0x1231, 0x2462, 0x48C4 )

# FUNCTION CreateXorArray_Method1
# PARAMETERS Password
# RETURNS array of 8-bit unsigned integers
# DECLARE XorKey AS 16-bit unsigned integer
# DECLARE ObfuscationArray AS array of 8-bit unsigned integers
# SET XorKey TO CreateXorKey_Method1(Password)
# SET Index TO Password.Length
# SET ObfuscationArray TO (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
# 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)
# IF Index MODULO 2 IS 1
# SET Temp TO most significant byte of XorKey
# SET ObfuscationArray[Index] TO XorRor(PadArray[0], Temp)
#         DECREMENT Index
# SET Temp TO least significant byte of XorKey
# SET PasswordLastChar TO Password[Password.Length MINUS 1] 
# SET ObfuscationArray[Index] TO XorRor(PasswordLastChar, Temp)
# END IF
#     WHILE Index IS GREATER THAN to 0
#         DECREMENT Index
# SET Temp TO most significant byte of XorKey
# SET ObfuscationArray[Index] TO XorRor(Password[Index], Temp)
#         DECREMENT Index
# SET Temp TO least significant byte of XorKey
# SET ObfuscationArray[Index] TO XorRor(Password[Index], Temp) 
# END WHILE
# SET Index TO 15
# SET PadIndex TO 15 MINUS Password.Length 
# WHILE PadIndex IS greater than 0
# SET Temp TO most significant byte of XorKey
# SET ObfuscationArray[Index] TO XorRor(PadArray[PadIndex], Temp) 
# DECREMENT Index
# DECREMENT PadIndex



# SET Temp TO least significant byte of XorKey
# SET ObfuscationArray[Index] TO XorRor(PadArray[PadIndex], Temp) 
# DECREMENT Index
# DECREMENT PadIndex
# END WHILE
#     RETURN ObfuscationArray
# END FUNCTION

# FUNCTION CreateXorKey_Method1 PARAMETERS Password
# RETURNS 16-bit unsigned integer
# DECLARE XorKey AS 16-bit unsigned integer
# SET XorKey TO InitialCode[Password.Length MINUS 1] 
# SET CurrentElement TO 0x00000068
# FOR EACH Char IN Password IN REVERSE ORDER FOR 7 iterations
# IF (Char BITWISE AND 0x40) IS NOT 0
# SET XorKey TO XorKey BITWISE XOR XorMatrix[CurrentElement]
#             END IF
#             SET Char TO Char MULTIPLIED BY 2
#             DECREMENT CurrentElement
#         END FOR
#     END FOR
#     RETURN XorKey
# END FUNCTION

# FUNCTION XorRor
# PARAMETERS byte1, byte2 RETURNS 8-bit unsigned integer
#     RETURN Ror(byte1 XOR byte2)
# END FUNCTION
# FUNCTION Ror
#     PARAMETERS byte
# RETURNS 8-bit unsigned integer
#     SET temp1 TO byte DIVIDED BY 2
#     SET temp2 TO byte MULTIPLIED BY 128
#     SET temp3 TO temp1 BITWISE OR temp2
#     RETURN temp3 MODULO 0x100
# END FUNCTION


# FUNCTION EncryptData_Method1
# PARAMETERS Password, Data, XorArrayIndex
# DECLARE XorArray as array of 8-bit unsigned integers
# SET XorArray TO CreateXorArray_Method1(Password)
# FOR Index FROM 0 TO Data.Length
# SET Value TO Data[Index]
# SET Value TO (Value rotate left 5 bits)
# SET Value TO Value BITWISE XOR XorArray[XorArrayIndex] SET DATA[Index] TO Value
#         INCREMENT XorArrayIndex
# SET XorArrayIndex TO XorArrayIndex MODULO 16 END FOR
# END FUNCTION


# FUNCTION DecryptData_Method1
# PARAMETERS Password, Data, XorArrayIndex
# DECLARE XorArray as array of 8-bit unsigned integers
# SET XorArray TO CreateXorArray_Method1(Password)
# FOR Index FROM 0 to Data.Length
# SET Value TO Data[Index]
# SET Value TO Value BITWISE XOR XorArray[XorArrayIndex] SET Value TO (Value rotate right 5 bits)
# SET Data[Index] TO Value
#         INCREMENT XorArrayIndex
# SET XorArrayIndex TO XorArrayIndex MODULO 16 END FOR
# END FUNCTION

FUNCTION CreatePasswordVerifier_Method1 PARAMETERS Password
    SET Verifier TO 0x0000
    SET PasswordArray TO (empty array of bytes) 
    SET PasswordArray[0] TO Password.Length 
    APPEND Password TO PasswordArray
    
    FOR EACH PasswordByte IN PasswordArray IN REVERSE ORDER 
        IF (Verifier BITWISE AND 0x4000) is 0x0000
            SET Intermediate1 TO 0
        ELSE
            SET Intermediate1 TO 1
        ENDIF
        
        SET Intermediate2 TO Verifier MULTIPLED BY 2 
        SET most significant bit of Intermediate2 TO 0
        
        SET Intermediate3 TO Intermediate1 BITWISE OR Intermediate2
        SET Verifier TO Intermediate3 BITWISE XOR PasswordByte 
    ENDFOR
    
    RETURN Verifier BITWISE XOR 0xCE4B
END FUNCTION



SET PadArray TO ( 0xBB, 0xFF, 0xFF, 0xBA, 0xFF, 0xFF, 0xB9, 0x80, 0x00, 0xBE, 0x0F, 0x00, 0xBF, 0x0F, 0x00 )
SET InitialCode TO
SET XorMatrix TO (
( 0xE1F0, 0x1D0F, 0xCC9C, 0x84C0, 0x110C, 0x0E10, 0xF1CE, 0x313E, 0x1872, 0xE139, 0xD40F, 0x84F9, 0x280C, 0xA96A, 0x4EC3 )
0xAEFC, 0x4DD9, 0x9BB2, 0x2745, 0x4E8A, 0x9D14, 0x2A09, 0x7B61, 0xF6C2, 0xFDA5, 0xEB6B, 0xC6F7, 0x9DCF, 0x2BBF, 0x4563, 0x8AC6, 0x05AD, 0x0B5A, 0x16B4, 0x2D68, 0x5AD0, 0x0375, 0x06EA, 0x0DD4, 0x1BA8, 0x3750, 0x6EA0, 0xDD40, 0xD849, 0xA0B3, 0x5147, 0xA28E, 0x553D, 0xAA7A, 0x44D5, 0x6F45, 0xDE8A, 0xAD35, 0x4A4B, 0x9496, 0x390D, 0x721A, 0xEB23, 0xC667, 0x9CEF, 0x29FF, 0x53FE, 0xA7FC, 0x5FD9, 0x47D3, 0x8FA6, 0x0F6D, 0x1EDA, 0x3DB4, 0x7B68, 0xF6D0, 0xB861, 0x60E3, 0xC1C6, 0x93AD, 0x377B, 0x6EF6, 0xDDEC, 0x45A0, 0x8B40, 0x06A1, 0x0D42, 0x1A84, 0x3508, 0x6A10,
0xAA51, 0x4483, 0x8906, 0x022D, 0x045A, 0x08B4, 0x1168, 0x76B4, 0xED68, 0xCAF1, 0x85C3, 0x1BA7, 0x374E, 0x6E9C, 0x3730, 0x6E60, 0xDCC0, 0xA9A1, 0x4363, 0x86C6, 0x1DAD, 0x3331, 0x6662, 0xCCC4, 0x89A9, 0x0373, 0x06E6, 0x0DCC, 0x1021, 0x2042, 0x4084, 0x8108, 0x1231, 0x2462, 0x48C4 )

FUNCTION CreateXorArray_Method1
PARAMETERS Password
RETURNS array of 8-bit unsigned integers
DECLARE XorKey AS 16-bit unsigned integer
DECLARE ObfuscationArray AS array of 8-bit unsigned integers
SET XorKey TO CreateXorKey_Method1(Password)
SET Index TO Password.Length
SET ObfuscationArray TO (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)
IF Index MODULO 2 IS 1
SET Temp TO most significant byte of XorKey
SET ObfuscationArray[Index] TO XorRor(PadArray[0], Temp)
        DECREMENT Index
SET Temp TO least significant byte of XorKey
SET PasswordLastChar TO Password[Password.Length MINUS 1] 
SET ObfuscationArray[Index] TO XorRor(PasswordLastChar, Temp)
END IF
    WHILE Index IS GREATER THAN to 0
        DECREMENT Index
SET Temp TO most significant byte of XorKey
SET ObfuscationArray[Index] TO XorRor(Password[Index], Temp)
        DECREMENT Index
SET Temp TO least significant byte of XorKey
SET ObfuscationArray[Index] TO XorRor(Password[Index], Temp) 
END WHILE
SET Index TO 15
SET PadIndex TO 15 MINUS Password.Length 
WHILE PadIndex IS greater than 0
SET Temp TO most significant byte of XorKey
SET ObfuscationArray[Index] TO XorRor(PadArray[PadIndex], Temp) 
DECREMENT Index
DECREMENT PadIndex



SET Temp TO least significant byte of XorKey
SET ObfuscationArray[Index] TO XorRor(PadArray[PadIndex], Temp) 
DECREMENT Index
DECREMENT PadIndex
END WHILE
    RETURN ObfuscationArray
END FUNCTION

FUNCTION CreateXorKey_Method1 PARAMETERS Password
RETURNS 16-bit unsigned integer
DECLARE XorKey AS 16-bit unsigned integer
SET XorKey TO InitialCode[Password.Length MINUS 1] 
SET CurrentElement TO 0x00000068
FOR EACH Char IN Password IN REVERSE ORDER FOR 7 iterations
IF (Char BITWISE AND 0x40) IS NOT 0
SET XorKey TO XorKey BITWISE XOR XorMatrix[CurrentElement]
            END IF
            SET Char TO Char MULTIPLIED BY 2
            DECREMENT CurrentElement
        END FOR
    END FOR
    RETURN XorKey
END FUNCTION

FUNCTION XorRor
PARAMETERS byte1, byte2 RETURNS 8-bit unsigned integer
    RETURN Ror(byte1 XOR byte2)
END FUNCTION
FUNCTION Ror
    PARAMETERS byte
RETURNS 8-bit unsigned integer
    SET temp1 TO byte DIVIDED BY 2
    SET temp2 TO byte MULTIPLIED BY 128
    SET temp3 TO temp1 BITWISE OR temp2
    RETURN temp3 MODULO 0x100
END FUNCTION


FUNCTION EncryptData_Method1
PARAMETERS Password, Data, XorArrayIndex
DECLARE XorArray as array of 8-bit unsigned integers
SET XorArray TO CreateXorArray_Method1(Password)
FOR Index FROM 0 TO Data.Length
SET Value TO Data[Index]
SET Value TO (Value rotate left 5 bits)
SET Value TO Value BITWISE XOR XorArray[XorArrayIndex] SET DATA[Index] TO Value
        INCREMENT XorArrayIndex
SET XorArrayIndex TO XorArrayIndex MODULO 16 END FOR
END FUNCTION


FUNCTION DecryptData_Method1
PARAMETERS Password, Data, XorArrayIndex
DECLARE XorArray as array of 8-bit unsigned integers
SET XorArray TO CreateXorArray_Method1(Password)
FOR Index FROM 0 to Data.Length
SET Value TO Data[Index]
SET Value TO Value BITWISE XOR XorArray[XorArrayIndex] SET Value TO (Value rotate right 5 bits)
SET Data[Index] TO Value
        INCREMENT XorArrayIndex
SET XorArrayIndex TO XorArrayIndex MODULO 16 END FOR
END FUNCTION