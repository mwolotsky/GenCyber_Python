def openFile(filename):
    file = open(filename,'r')
    stuff = file.read()
    file.close()
    return stuff

def decrypt(cipherText):
    plainText = ""
    i = 1
    for c in cipherText:
        plainText += chr(ord(c) ^ i)
        i += 3
    return plainText

Info = ["" for i in range(30)] + ["","","b","o","r","i","n","g",".","t","x","t"]

name = raw_input("Enter Your Name: ")

Stuff = list(name) + Info[len(name):]

print "The Array Storing your name and the file information is:"
print Stuff

print

print "Hello %s, The File Contents Are:" % name
print decrypt(openFile("".join(Stuff[30:])))

