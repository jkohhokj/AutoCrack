import string
from datetime import datetime
def xor(message,key,output="b",delimiter=' '):
    finished = []
    if output == "l":
        for charIndex in range(len(message)):
            finished.append(chr(ord(message[charIndex]) ^ ord(key[charIndex%len(key)])))
        return delimiter.join(finished)
    if output == "d":
        for charIndex in range(len(message)):
            finished.append(ord(message[charIndex]) ^ ord(key[charIndex%len(key)]))
        return delimiter.join(finished)
    if output == "b":
        for charIndex in range(len(message)):
            finished.append(bin(ord(message[charIndex]) ^ ord(key[charIndex%len(key)])))
        return delimiter.join(finished)
    #if output == "b":
    #    #print(delimiter.join([bin(ord(char) ^ ord(key)) for char in message]))
    #    return delimiter.join([bin(ord(char) ^ ord(key)) for char in message])
    #if output == "d":
    #    #print(delimiter.join([str(ord(char) ^ ord(key)) for char in message]))
    #    return delimiter.join([str(ord(char) ^ ord(key)) for char in message])
    #if output == "l":
    #    #print(delimiter.join([chr(ord(char) ^ ord(key)) for char in message]))
    #    return delimiter.join([chr(ord(char) ^ ord(key)) for char in message])


def autoXor(message,keyword,min=2,max=5):
    max += 1
    old = datetime.now()
    #print(message)
    for length in range(min,max):
        for key in range(1,255):    
            #print(chr(key),bin(key))
            #print(xor(message,chr(key),"l",""))
            if keyword in xor(message,chr(key),"l",""):
                #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                print(xor(message,chr(key),"l",""), ", key is: ", bin(key))