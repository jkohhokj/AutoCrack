import string
from datetime import datetime
from BruteForceLetter import bruteForceLetter
def vigenereEncode(message,key):
    #print("tried",key)
    message = message.upper()
    key = key.upper()
    numToLet = dict(zip([x for x in range(26)],list(string.ascii_uppercase)))
    letToNum = dict(zip(list(string.ascii_uppercase),[x for x in range(26)]))
    # set up the table
    decoded = []
    for charIndex in range(len(message)):
        #print("first",letToNum[str(message[charIndex])])
        #print("second",letToNum[str(key[keyIndex])])
        #print("newNum",letToNum[message[charIndex]]+letToNum[key[keyIndex%len(key)]])
        #print("newLet",numToLet[(letToNum[message[charIndex]]+letToNum[key[charIndex%len(key)]])%26])
        decoded.append(numToLet[(letToNum[message[charIndex]]+letToNum[key[charIndex%len(key)]])%26])
    # translate the message
    return ''.join(decoded)
def vigenereDecode(message,key): # literally change the plus to minus
    message = message.upper()
    key = key.upper()
    numToLet = dict(zip([x for x in range(26)],list(string.ascii_uppercase)))
    letToNum = dict(zip(list(string.ascii_uppercase),[x for x in range(26)]))
    # set up the table
    decoded = []
    for charIndex in range(len(message)):
        if message[charIndex] in string.ascii_uppercase:
        #print("first",letToNum[str(message[charIndex])])
        #print("second",letToNum[str(key[keyIndex])])
        #print("newNum",letToNum[message[charIndex]]+letToNum[key[keyIndex%len(key)]])
        #print("newLet",numToLet[(letToNum[message[charIndex]]+letToNum[key[charIndex%len(key)]])%26])
            decoded.append(numToLet[(letToNum[message[charIndex]]-letToNum[key[charIndex%len(key)]])%26])
        else:
            decoded.append(message[charIndex])
    # translate the message
    return ''.join(decoded)
def autoVigenere(message,keyword,min=2,max=5): #3=.8;4=21;5=10:40;6=4:40:00
    old = datetime.now()
    #modMessage = []
    #for word in message.split():
    #    if len(word) == len(keyword):
    #        modMessage.append(word)
    #modMessage = ' '.join(modMessage)
    #print(modMessage) #change message to modMessage in for loop in message
    message = message.upper()

    max += 1
    for length in range(min,max):
        for key in bruteForceLetter(length):
            #print("keyword encoded: ",vigenereEncode(keyword,key),' ',"")
            #print(vigenereEncode(keyword,key))
            #print(message)
            if vigenereEncode(keyword,key) in message:
                print("decoded: ",vigenereDecode(message,key)," ","key: ",key)
                print(datetime.now()-old)
                return vigenereDecode(message,key)