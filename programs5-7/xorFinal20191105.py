#############################################################################################################
# Team: 1
# Member Names: Andrew Almond, Clark Foster, Luke Seaton, Samuel Spohn, Christian Thibodeaux, Anthony Toussaint
# GitHub: https://github.com/samcspohn/CSC-442
# Date: 24 Oct 2019
# Description: XOR Encryption
# Python Version: 3.7 
#############################################################################################################

DEBUG = False

# import libraries
import sys
import binascii
import os

##########################################INPUT KEY###########################################################
# Name of the key file
KEY = "key2"

# Read date from key, which is a file in the current directory
k = open(KEY,"rb")  #rb reads the binary
# Check that the file is in open mode
if k.mode == 'rb':
    # if so, read the contents of the file and store it in variable
     contents = k.read()
    
# Convert to bytearray
byteArrayK = bytearray(contents)


# Debug option, displays byte number
if DEBUG:
     bytesK=0
     for byte in byteArrayK:
          bytesK +=1

     print(bytesK)

#############################################INPUT MESSAGE######################################################

# Read the data from stdin as binary data
m = sys.stdin.buffer.read()

# Convert m to bytearray
byteArrayM  = bytearray(m)

# Debug option, displays byte number
if DEBUG:
     bytesM=0
     for byte in byteArrayM:
          bytesM +=1

     print(bytesM)


##########################################XOR each byte array object with the other and print ###################


for i in range(len(byteArrayK)):
     byteArrayM[i] ^= byteArrayK[i]

#fp = os.fdopen(sys.stdout.fileno(),'wb')

# write result to stdout
#fp.write(byteArrayM)

# write result to stdout
sys.stdout.buffer.write(byteArrayM)

# if image, save to file for viewing
f = open('xorimage.jpeg','wb')
f.write(byteArrayM)
f.close()

     

