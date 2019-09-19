import sys

s = sys.stdin.read() # f.readline()

hasReturn = 0
if(s[-1] == '\r' or s[-1] == '\n'):
    hasReturn = 1
if((len(s) - hasReturn) % 7 == 0):
    c = 7
    for i in range(int(len(s) / c)):
        print(chr(int(s[i*c:i*c + c],2)), end='')
    print("")

if((len(s)- hasReturn) % 8 == 0):
    c = 8
    for i in range(int(len(s) / c)):
        print(chr(int(s[i*c:i*c + c],2)), end='')
    print("")
    