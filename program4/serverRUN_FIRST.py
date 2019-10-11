#############################################################################################################
# Team: 1
# Member Names: Andrew Almond, Clark Foster, Luke Seaton, Samuel Spohn, Christian Thibodeaux, Anthony Toussaint
# GitHub: https://github.com/samcspohn/CSC-442
# Date: 8 Oct 2019
# Description: FTP Covert Message Extraction, Decode
# Python Version: 3.7 
#############################################################################################################

# This file acts as the server sending the message to be decoded by the other file


# IMPORTANT NOTE: PLEASE RUN THIS FILE IN SEPARATE TERMINAL IN ORDER AND RUN
# THE OTHER FILE WHICH DECODES IT IN ANOTHER TERMINAL

#import libraries
import socket
import time
from binascii import hexlify

# set up the server
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 1337
    s.bind(("", port))
    s.listen(0)
except:
    close()

c, addr = s.accept()

# initialize the time delays
ZERO = .025
ONE = .1

# initialize overt and covert messages
msg = "My name is Happy Gilmore. Ever since I was old enough to skate, I loved hockey... wasn't the greatest skater though. But that didn't stop my dad from teaching me the secret of slapping the greatest slapshot. My dad worshiped hockey, my mom didn't, that's why she moved to Egypt, where there's not a hockey rink within 15 hundred miles."
covert = "I still feel I won the fight." + "EOF"

# initialize covert message binary string
covert_bin = ""

# convert covert message to binary message via time delays
for i in covert:
    covert_bin += bin(int(hexlify(i), 16))[2:].zfill(8) #16 because hex
n = 0
for i in msg:
    c.send(i)
    if(covert_bin[n] == "0"):
        time.sleep(ZERO)
    else:
        time.sleep(ONE)
    n = (n + 1) % len(covert_bin)


# send EOF and close out server
c.send("EOF")
c.close()
