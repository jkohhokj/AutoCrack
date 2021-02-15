import string
from datetime import datetime
def caesar(message,rot):
    original = list(string.ascii_lowercase+string.ascii_uppercase)
    new = []
    for x in range(26):
        if rot+x < 26:
            new.append(original[rot+x])
        else:
            new.append(original[rot+x-26]) # starts over from the beginning
    for x in range(26):
        if rot+x < 26:
            new.append(original[rot+x+26])
        else:
            new.append(original[rot+x]) # +26-26 cancel out and starts over from the beginning
    table = dict(zip(original,new))
    # set up the table of rot
    decoded = []
    for char in message:
        if char in original:
            decoded.append(table[char])
        else:
            decoded.append(char)
    # translate the message 
    return ''.join(decoded)
def autoCaesar(message,keyword,showTime=False):
    old = datetime.now()
    for rot in range(26):
        encoded = caesar(keyword,rot)
        if encoded in message:
            print(encoded, " in ", message)
            print(caesar(message,26-rot))
            if showTime:
                print(datetime.now()-old)
            return caesar(message,26-rot)
