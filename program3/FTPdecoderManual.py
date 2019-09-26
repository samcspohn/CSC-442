#############################################################################################################
# Team: 1
# Member Names: Andrew Almond, Clark Foster, Luke Seaton, Samuel Spohn, Christian Thibodeaux, Anthony Toussaint
# GitHub: https://github.com/samcspohn/CSC-442
# Date: 26 Sept 2019
# Description: FTP Covert Message Extraction, Decode
# Python Version: 3.7 
#############################################################################################################


# import FTP library
from ftplib import FTP
import ftplib

# connect to and login to FTP
ftp = FTP('jeangourd.com')
ftp.connect('jeangourd.com')
ftp.login()

METHOD = "10"

if METHOD == "10":

    # instantiate a list for file permissions in the 10 bit directory
    list10 = []

    # navigate to 10bit directory and append contents to a list
    ftp.cwd(METHOD) 
    ftp.retrlines('LIST', list10.append)

    # now that we have our information, get off the FTP ASAP
    ftp.quit()
    ftp.close()

    # now concatenate permissions into a string (utilizing all 10 bits)
    concatList10 = ""
    for item in list10:
        concatList10 += item[0:10]


    # convert the string to a list of characters
    concatList10 = list(concatList10)


    # converts dashes to 0's and all others to 1s
    for i in range(len(concatList10)):
        if concatList10[i] == '-':
            concatList10[i] = 0
        else:
            concatList10[i] = 1

    # initialize an empty string and concatenate all bits to it
    binString = ""
    for i in range(len(concatList10)):
        binString += str(concatList10[i])



    # now decode the binary message
    finalString = ""
    for i in range(len(binString)-1):
        # if the character in the string is the first of a group of 7(from notes),
        # then initialize an empty string 
        if i==0 or i%7 == 0:
            asciVal = 0
            tempString = ""

            # concatonate the 1st character of each 10bit set and the next 6
            j = 0
            while j<=6:
                try:
                    tempString += binString[i+j]
                except IndexError:
                    break
                j += 1

            #print(tempString)



            # now calculate the decimal value (ascii val) of each 7bit binary set
            m = 6
            n = 0
            while m>=0:
                try:
                    if int(binString[i+m]) == 1:
                        asciVal += 2**n
                except IndexError:
                    break
                m-=1
                n+=1

            #print(asciVal)

            char = chr(asciVal)

            #if char is a backspace, then dont print it, and slice the last character all
            # of the final string
            if asciVal == 8:
                finalString = finalString[:-1]

            else:
                finalString += char

    print(finalString)






if METHOD == "7":

    # instantiate a list for file permissions in the 7 bit directory
    list7 = []

    # navigate to 7 bit directory and append contents to a list
    ftp.cwd(METHOD) 
    ftp.retrlines('LIST', list7.append)

    # now that we have our information, get off the FTP ASAP
    ftp.quit()
    ftp.close()

    #remove all permission lines where 1st three letters are not ---              ###############################################
    for item in list7:
        if item[0:3] != '---':
            list7.remove(item)

    for item in list7:
        if item[0:3] != '---':
            list7.remove(item)

    # now concatenate permissions into a string (from 3rd position to 10th exclusive)
    concatList7 = ""
    for item in list7:
        concatList7 += item[3:10]


    # convert the string to a list of characters
    concatList7 = list(concatList7)


    # converts dashes to 0's and all others to 1s
    for i in range(len(concatList7)):
        if concatList7[i] == '-':
            concatList7[i] = 0
        else:
            concatList7[i] = 1

    # initialize an empty string and concatenate all bits to it
    binString = ""
    for i in range(len(concatList7)):
        binString += str(concatList7[i])



    # now decode the binary message
    finalString = ""
    for i in range(len(binString)-1):
        # if the character in the string is the first of a group of 10,
        # then initialize an empty string
        if i==0 or i%7 == 0:
            asciVal = 0
            tempString = ""

            # concatonate the 1st character of each 10bit set and the next 9
            j = 0
            while j<=6:
                try:
                    tempString += binString[i+j]
                except IndexError:
                    break
                j += 1


            # now calculate the decimal value (ascii val) of each 10bit binary set
            m = 6
            n = 0
            while m>=0:
                try:
                    if int(binString[i+m]) == 1:
                        asciVal += 2**n
                except IndexError:
                    break
                m-=1
                n+=1

            char = chr(asciVal)

            #if char is a backspace, then dont print it, and slice the last character all
            # of the final string
            if asciVal == 8:
                finalString = finalString[:-1]

            else:
                finalString += char

    print(finalString)

