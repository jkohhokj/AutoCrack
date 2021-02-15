import os
import string
from datetime import datetime
from BruteForceLetter import bruteForceLetter
from Vigenere import autoVigenere
from Caesar import autoCaesar
from Xor import autoXor
from datetime import datetime


if __name__ == "__main__":
    #caesar("rkeqEVH{vlfal}",24)
    autoCaesar("rkeqEVH{vlfal}","picoCTF")
    #print(vigenereDecode("selpjzhfxkftyulwmcgmfkeybo","abcfdhdfg"))
    #print([x for x in bruteForceLetter(4)])
    #autoVigenere("ogznaqe ffnfdzqe vbbnfg rmahfcz jbhuo ibyrdpcllllllllllllll lllllllllllllll llllllllllll llllllllllllll lllllllllllllllllll llllllllllllllll llllll","picoctf",min=3,max=3)
    #xor("abcdef","B")
    #xor("abcdef","B",'d')
    #xor("abcdef","B",'l','')
    #xor("# !&'$","B",'l')
    #print(bin(ord("a")))
    #print(bin(ord("A")))
    #autoXor("# !&'$","abc",2)
    #print(vigenereEncode("picoctf","abc"))
    #