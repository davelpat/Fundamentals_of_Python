"""
Instructions for programming Exercise 5.2

Write a program that allows the user to navigate the lines of text in a file.
The program should prompt the user for a filename and input the lines of text
into a list. The program then enters a loop in which it prints the number of
lines in the file and prompts the user for a line number. Actual line numbers
range from 1 to the number of lines in the file. If the input is 0, the program
quits. Otherwise, the program prints the line associated with that number.

An example file and the program input and output is shown below:

example.txt

Line 1.
Line 2.
Line 3.

Enter the input file name: example.txt

The file has 3 lines.
Enter a line number [0 to quit]: 2
2 :  Line 2.
The file has 3 lines.
Enter a line number [0 to quit]: 0
"""

inputFile = input("Enter the input file name: ")

fIn = open(inputFile, "r")

lines = []
for inLine in fIn:
    lines.append(inLine)

lcnt = len(lines)
while True:
    print("The file has", lcnt, "lines.")
    lineNo = int(input("Enter a line number [0 to quit]: "))
    if lineNo == 0:
        break
    else:
        # lineNo += 1
        print(lineNo, ": ", lines[lineNo - 1])
