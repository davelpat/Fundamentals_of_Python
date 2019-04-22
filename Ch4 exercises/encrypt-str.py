"""
Instructions for programming Exercise 4.6

Use the strategy of the decimal to binary conversion and the bit shift left
operation defined in Project 5 to code a new encryption algorithm.

The algorithm should

Add 1 to each character’s numeric ASCII value.
Convert it to a bit string.
Shift the bits of this string one place to the left.
A single-space character in the encrypted string separates the resulting bit strings.

An example of the program input and output is shown below:

Enter a message: Hello world!

0010011 1001101 1011011 1011011 1100001 000011 1110001 1100001 1100111 1011011 1001011 000101
"""

DIST = 1
FIRST_ORD = 0
LAST_ORD = 127
SPACE = " "

txt = input("Enter a message: ")

eTxt = ""
for char in txt:
    # get and increment character's ASCII value
    charOrd = ord(char) + DIST
    # Not sure if the wrap around is required
    if charOrd > LAST_ORD:
        charOrd = FIRST_ORD + LAST_ORD - charOrd
    # Convert it to a bit string
    bstring = ""
    while charOrd > 0:
        remainder = charOrd % 2
        charOrd = charOrd // 2
        bstring = str(remainder) + bstring
    # Shift bit string 1 to the left
    bstring = bstring[DIST:len(bstring)]+bstring[0:DIST]
    eTxt += bstring + SPACE

print(eTxt)