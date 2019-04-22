"""
Instructions for programming Exercise 4.9

Write a script named copyFile.py. This script should prompt the user for the
names of two text files. The contents of the first file should be input and
written to the second file.

An example of the program input is shown below:

Enter the input file name: copyFrom.txt Enter the output file name: copyTo.txt
Output: The program should then create a file named copyTo.txt that contains the
text from copyFrom.txt.
"""

inputFile = input("Enter the input file name: ")
outputFile = input("Enter the output file name: ")

fIn = open(inputFile, "r")
fOut = open(outputFile, "w")

for inLine in fIn:
    fOut.write(inLine)

fIn.close
fOut.close
