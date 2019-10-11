#############################################################################################################
# Team: 1
# Member Names: Andrew Almond, Clark Foster, Luke Seaton, Samuel Spohn, Christian Thibodeaux, Anthony Toussaint
# GitHub: https://github.com/samcspohn/CSC-442
# Date: 8 Oct 2019
# Description: FTP Covert Message Extraction, Decode
# Python Version: 3.7 
#############################################################################################################


# This file extracts an overt as well as a covert message from a given server

# import libraries
import socket
import time
from time import time
import binascii
import sys

Debug = False

# first create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# initialize the ip and port
ip = "192.168.1.100"
port = 31337

# connect to the server on some ip and port
s.connect((ip, port))               

# message has delay between characters
ZERO = 0.025
ONE = 0.1

# initialize covert bin
covert_bin = ""
data = s.recv(4096)

while (data.rstrip(b"\n") != b"EOF"):   #had to add b because expecting byte object

    # display the overt message
    sys.stdout.write(data.decode('utf-8'))         #must decode the data so doesn't have 'b' prefix
    sys.stdout.flush()

    # now we get the binary covert message based on time delays
    t0 = time()
    data = s.recv(4096)
    t1 = time()
    delta = round(t1 - t0, 3)            
    if (delta >= ONE):
        covert_bin += "1"
    else:
        covert_bin += "0"

    #If Debug is set to true, the program will print out the delay next to each character
    if(Debug): 
        sys.stdout.write(" " + str(delta))         
        sys.stdout.write('\n') 
        sys.stdout.flush()
   

#close connection to server
s.close()

# now we convert the binary string to ASCII
covert = ""
i = 0
while (i < len(covert_bin)):
    # process one byte at a time
    b = covert_bin[i:i + 8]             # b becomes a set of 8 bits on each loop, 1st list item is i, followed by the remaining items of the 8-bit string
    # convert it to ASCII
    n = int("0b{}".format(b), 2)        # n becomes an integer representation of 8-bit binary number b, hence .format(b) and it must be prefaced with 0b to later tell unhexlify() function that it is a binary number, the 2 is the arguements base (base 2, binary) 
    if covert_bin[i:i+24] == "010001010100111101000110": #binary representation of EOF, written as a string because covert_bin is a string
        break;
    else:
        try:
            covert += binascii.unhexlify('{0:x}'.format(n))      
        except TypeError:                               # TypeError is raised when passing arguments of the wrong type (e.g. passing a list when an int is expected) 
            covert += "?"
        # stop at the string "EOF"
    i += 8


print("\nCovert Message: " + covert)
