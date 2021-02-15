import string
from datetime import datetime
def bruteForceLetter(length, beg=""):
    oldBeg = beg.upper()
    if length != 1:
        for x in string.ascii_uppercase:
            yield from bruteForceLetter(length-1, beg=oldBeg+x)
    else:
        for x in string.ascii_uppercase:
            yield oldBeg+x