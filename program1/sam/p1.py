import sys

s = sys.stdin.read() # f.readline()

hasReturn = 0
if(s[-1] == '\r' or s[-1] == '\n'):
    hasReturn = 1
lenS = len(s) - hasReturn
if(lenS % 7 == 0):
    c = 7
    for i in range(int(lenS / c)):
        print(chr(int(s[i*c:i*c + c],2)), end='') # take 7 bit chunks of input string, convert to int, convert to char. print to console. backspace moves cursor back
    print("")

if(lenS % 8 == 0):
    c = 8
    for i in range(int(lenS / c)):
        print(chr(int(s[i*c:i*c + c],2)), end='') 
    print("")
    