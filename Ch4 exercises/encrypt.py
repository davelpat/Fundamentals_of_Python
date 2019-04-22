"""
Instructions for programming Exercise 4.1

Write a script that inputs a line of plaintext and a distance value and outputs
an encrypted text using a Caesar cipher.

The script should work for any printable characters.

An example of the program input and output is shown below:

Enter a message: Hello world!
Enter the distance value: 4

Lipps${svph%
"""

txt = input("Enter a message: ")
dist = int(input("Enter the distance value: "))

firstOrd = ord(' ')
lastOrd = ord('~')
eTxt = ""
for char in txt:
    charOrd = ord(char)
    eOrd = charOrd + dist
    if eOrd > lastOrd:
        eOrd = firstOrd + lastOrd - charOrd
    eTxt += chr(eOrd)

print(eTxt)