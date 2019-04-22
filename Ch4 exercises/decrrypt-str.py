"""
Instructions for programming Exercise 4.7

Write a script that decrypts a message coded by the method used in Project 6.

Method used in project 6:

Add 1 to each character’s numeric ASCII value.
Convert it to a bit string.
Shift the bits of this string one place to the left.
A single-space character in the encrypted string separates the resulting bit strings.

An example of the program input and output is shown below:

Enter the coded text: 0010011 1001101 1011011 1011011 1100001 000011 1110001 1100001 1100111 1011011 1001011 000101

Hello world!
"""

DIST = 1
FIRST_ORD = 0
LAST_ORD = 127
SPACE = " "

charList = input("Enter the coded text: ").split()

eTxt = ""
for bstring in charList:
    # Shift bit string 1 to the left
    bStrSize = len(bstring)
    bstring = bstring[-DIST:bStrSize] + bstring[0:bStrSize - DIST]
    # Convert ordinal bit string to decimal
    charOrd = 0
    exponent = bStrSize - 1
    for digit in bstring:
        charOrd = charOrd + int(digit) * 2 ** exponent
        exponent = exponent - 1
    # Readjust ordinal value
    eTxt += chr(charOrd - 1)

print(eTxt)