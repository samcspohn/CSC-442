
METHOD = 7

# open text file and create new file for edited string
test = 'testFile.txt'
with open(test) as tf:
    temp = open("tempFile.txt", "a+")
    line = tf.readline()

# read line by line
# replace "-" with "0" (replacing characters hasn't been implemented yet)
# strip excess parts off

    while line != "":
        strip = line.strip()
        temp.write("{}".format((strip[10-METHOD:10]).replace("-", "0")))
        line = tf.readline()

    temp.close()
