# The Celts
# Github Link: https://github.com/samcspohn/CSC-442.git

import sys
import time
import datetime
import hashlib

TESTCURRENT = True # Use current time (True) or given time (False)

def UTC(s): # Convert DST to UTC
    secs = time.mktime(s)
    r = time.gmtime(secs)
    return time.mktime(r) # Return UTC in seconds

#epoch = str(input())
epoch = raw_input()
#epoch = "2019 01 22 04 32 16"


if (TESTCURRENT == True):
    current = datetime.datetime.now()
    current = current.strftime('%Y %m %d %H %M %S')
else:
    current = "2019 10 20 12 00 00"

epochDate = datetime.datetime.strptime(epoch, '%Y %m %d %H %M %S') # Format string to date
currentDate = datetime.datetime.strptime(current, '%Y %m %d %H %M %S')


startTime = UTC(epochDate.timetuple()) # Convert to tuple and return in UTC form
endTime = UTC(currentDate.timetuple())

total = endTime - startTime # Find difference in epoch and current

if (total % 60 != 0): # Checks if the number of seconds is not divisible by 60
    total = int(total / 60) # Divide by 60 and remove numbers after decimal point
    total = total * 60 # This is meant to get a number within 60 sec interval
else:
    total = int(total) # Remove numbers after decimal point

Alpha = "" # Store all letters in hash
Num = "" # Store all numbers in hash

md5 = hashlib.md5(str(hashlib.md5(str(total)).hexdigest())).hexdigest() # number of seconds twice

for i in md5: # Parses through hash
    if (i.isalpha() == True): # Make sure we don't have '1 in 3.4 million' case
        Alpha += i # Adds letter to Alpha
    else:
        Num += i # Add numbers to Num

#print(md5)

print(Alpha[:2] + Num[-1] + Num[-2])

