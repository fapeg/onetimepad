#!/usr/bin/python
import string, sys
from random import choice

letterlist = string.lowercase

def create_random_string(laenge):
    random_string = ""
    i=0
    for i in xrange(laenge):
        random_string+=choice(letterlist)
    return random_string
    
def many_strings(laenge, anzahl):
    i=0
    allentries = []
    for i in xrange(anzahl):
        rowstring = str(i+1)+".: " + create_random_string(laenge)
        print rowstring
        allentries.append(rowstring)
    with open('otpkeys.txt', 'w+') as f:
        for row in allentries:
            f.write(row+"\n")
            
            
def generate_password(laenge):
    satzzeichen = "!#$%&()*+,-./:;<=>?@[]_{|}~"
    p_string = string.ascii_letters + string.digits + satzzeichen + string.ascii_letters + string.digits 
    x=0
    satzzeichen_count = 0
    while satzzeichen_count < 2:
        satzzeichen_count = 0
        password = ""
        for x in xrange(laenge):
            password +=choice(p_string)
        for z in password:
            if z in satzzeichen:
                satzzeichen_count += 1
    if __name__ == "__main__":
        print password
    return password
    
if __name__ == "__main__":
    if (len(sys.argv)) == 2:
        l = int(sys.argv[1])
        generate_password(l)