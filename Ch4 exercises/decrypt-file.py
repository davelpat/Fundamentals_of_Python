"""
Instructions

Modify the scripts of Projects 1 and 2 to encrypt and decrypt entire files of text.

An example of the program interface is shown below:

Enter the input file name: encrypted.txt
Enter the output file name: a
Enter the distance value: 3
"""

"""
File: decrypt-file.py
Project 4.3

Decrypts a file of the ASCII characters and outputs
the result to another file.  The other input is the
distance value.
"""

# The ASCII values range from 0 through 127

inputFile = input("Enter the input file name: ")
outputFile = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))

fIn = open(inputFile, "r")
fOut = open(outputFile, "w")

for inLine in fIn:
    for ch in inLine:
        ordValue = ord(ch)
        cipherValue = ordValue - distance
        if cipherValue < 0:
            cipherValue = 127 - \
                          (distance - (1 - ordValue))
        fOut.write(chr(cipherValue))

fIn.close
fOut.close
