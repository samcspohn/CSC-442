
METHOD = 7

test = 'testFile.txt'
with open(test) as tf:
    temp = open("tempFile.txt", "a+")
    line = tf.readline()

    while line != "":
        strip = line.strip()
        temp.write("{}".format((strip[10-METHOD:10]).replace("-", "0")))
        print("{}".format(line.strip()))
        line = tf.readline()

    string = ("{}".format(temp))

    print(string)
    temp.close()
