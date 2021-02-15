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
    encoded = []
    for charIndex in range(len(message)):
        if message[charIndex] in string.ascii_uppercase:
            #human readable one is commented
            #firstLetNum = letToNum[str(message[charIndex])]
            #secondLetNum = letToNum[str(key[charIndex%len(key)])]
            #newNum = (firstLetNum + secondLetNum)%26
            #newLet = numToLet[newNum]
            #encoded.append(newLet)
            encoded.append(numToLet[(letToNum[message[charIndex]]+letToNum[key[charIndex%len(key)]])%26])
        else:
            encoded.append(message[charIndex])
    return ''.join(encoded)
def vigenereDecode(message,key): # literally change the plus to minus
    message = message.upper()
    key = key.upper()
    numToLet = dict(zip([x for x in range(26)],list(string.ascii_uppercase)))
    letToNum = dict(zip(list(string.ascii_uppercase),[x for x in range(26)]))
    # set up the table
    decoded = []
    for charIndex in range(len(message)):
        if message[charIndex] in string.ascii_uppercase:
            # human readable one is commented
            #firstLetNum = letToNum[str(message[charIndex])]
            #secondLetNum = letToNum[str(key[charIndex%len(key)])]
            #newNum = (firstLetNum - secondLetNum)%26
            #newLet = numToLet[newNum]
            #encoded.append(newLet)
            decoded.append(numToLet[(letToNum[message[charIndex]]-letToNum[key[charIndex%len(key)]])%26])
        else:
            decoded.append(message[charIndex])
    return ''.join(decoded)
def autoVigenere(message,keyword,min=2,max=5,showTime=False): #3=.8;4=21;5=10:40;6=4:40:00
    old = datetime.now()
    message = message.upper()
    max += 1
    for length in range(min,max):
        for key in bruteForceLetter(length):
            if vigenereEncode(keyword,key) in message:
                print("decoded: ",vigenereDecode(message,key)," ","key: ",key)
                if showTime:
                    print(datetime.now()-old)
                return vigenereDecode(message,key)
