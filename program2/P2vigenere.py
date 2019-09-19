#############################################################################################################
#Group 1
#Names: Andrew Almond, Clark Foster, Luke Seaton, Samuel Spohn, Christian Thibodeaux, Anthony Toussaint
#GitHub: https://github.com/samcspohn/CSC-442
#Date: 19 Sept 2019
#############################################################################################################

import sys

###I use dictionaries here to associate the letters with the numbers and vice versa. 
alphabetDict = {
	"a" : 1,
	"b" : 2,
	"c" : 3,
	"d" : 4,
	"e" : 5,
	"f" : 6,
	"g" : 7,
	"h" : 8,
	"i" : 9,
	"j" : 10,
	"k" : 11,
	"l" : 12,
	"m" : 13,
	"n" : 14,
	"o" : 15,
	"p" : 16,
	"q" : 17,
	"r" : 18,
	"s" : 19,
	"t" : 20,
	"u" : 21,
	"v" : 22,
	"w" : 23,
	"x" : 24,
	"y" : 25,
	"z" : 26,
	#"z" : 0,
	" " : 27
}


#This dictionary has some unique attributes. 1-26 are all unique, and nothing can go above 26 using the math below. 
#However, the math does allow for 0 and -1. If 1 is 'a', then 0 loops back to 'z' and -1 is 'y'. I use 27 to store an empty space.
numberDict = {
	-1: "y",
	0 : "z",
	1 : "a",
	2 : "b", 
	3 : "c",
	4 : "d",
	5 : "e",
	6 : "f",
	7 : "g",
	8 : "h",
	9 : "i",
	10 : "j",
	11 : "k",
	12 : "l",
	13 : "m",
	14 : "n",
	15 : "o",
	16 : "p",
	17 : "q",
	18 : "r",
	19 : "s",
	20 : "t",
	21 : "u",
	22 : "v",
	23 : "w",
	24 : "x",
	25 : "y",
	26 : "z",
	27 : " "
}


#The below function (sys.argv[]) takes the input from command line and saves it in a list.
#Index 0 is the file being executed, and index 1+ are the parameters seperated by spaces.
#For the keyword, I eliminate all spaces.
encode = sys.argv[1]
keyword = sys.argv[2].replace(" ", "")

#A While(True) loop which executes until a keyboard interrupt comes around.
while(True):
	try:
		codeWord = input() #Waits for an input followed by enter and saves it as the code-word.
	except:
		exit()

	numberCode = [] #List to store the number equivalents of the code-word's letters. A becomes 1, b becomes 2, etc.
	numberKey = [] #List to store the number equivalents of the keywords's letters. A becomes 1, b becomes 2, etc.

	postCipher = [] #List to store the number calculated below, which is associated with the encoded/decoded final product.
	output = "" #A string that stores the final output.
	
	capitalization = [] #A list that saves whether each value should be capitalized or not as True/False.

	i = 0 #Initialize the index variable.

	#Since non-letters in the codeword are not shifted, there needs to be a way to ensure the key-word is at the right spot. Thats this.
	#As an example, Lets say the key is "New" and the codeword is "I am." In this instance, index 0 of the codeword is I, index[1] is " ", 2 is 'a' and 3 is 'm'.
	#So, 'n' is used to offset 'I'. Both are index 0 of their respective terms (codeword/keyword). The space at index 1 of the codeword makes things odd.
	#The space is not decoded, and the keyword should not advance. So the 'a' in the codeword (index 2) is decoded by the 'e' in the keyword (index 1).
	#In this way, receiving any non-alphabet character needs to delay the index of the keyword behind the codeword by 1.
	#All of this is what the below variable "spaceOffset" is for. Always starts at 0.
	spaceOffset = 0 
	
	#Logic for encoding/decoding. Iterates through the codeword string.
	#Saves the current letter of the keyword first.
	#Then determines whether the current letter of the codeword is alphabet or symbol/number. Increases the offset if non-alphabet.
	#If it is alphabet, then it converts the current letter of the keyword and codeword to numbers and saves them as let0 and let1.
	#It then checks what the encoding param was and either encodes or decodes. Then it checks to see if the letter was capitalized and saves it.
	
	for x in codeWord:
		keywordLetter = keyword[(i - spaceOffset) % len(keyword)]
		
		if (not x.isalpha()):
			postCipher.append(str(x))
			capitalization.append(False)
			spaceOffset+=1
		elif x.lower() not in alphabetDict:
			postCipher.append(str(x))
			capitalization.append(False)
			spaceOffset+=1
		else:
			let0 = alphabetDict[x.lower()]
			let1 = alphabetDict[keywordLetter.lower()]	
			numberCode.append(let0)
			numberKey.append(let1)
			if(x == " "):
				postCipher.append(27)
			elif(encode == "-e"):
				postCipher.append(((let0 + let1) % 26) - 1)
				#postCipher.append(((let0 + let1) % 26) - 1)
			elif(encode == "-d"):
				postCipher.append(((let0 - let1) % 26) + 1)
			else:
				print("The first argument should be -e or -d.")
				exit()
			if(not x.islower() and x != " "):
				capitalization.append(True)
			else:
				capitalization.append(False)
		i += 1

	i = 0
	for x in postCipher:
		if(isinstance(x, str)):
			outputLetter = x
			output += outputLetter
		else:
			outputLetter = numberDict[x]
			if(capitalization[i]):
				outputLetter = outputLetter.upper()
			output += outputLetter
		i += 1

	print(output)


print("Exiting...")
