"""
Instructions for programming Exercise 4.2

Write a script that inputs a line of encrypted text and a distance value and
outputs plaintext using a Caesar cipher.

The script should work for any printable characters.

An example of the program input and output is shown below:

Enter the coded text: Lipps${svph%
Enter the distance value: 4

Hello world!
"""

txt = input("Enter a message: ")
dist = int(input("Enter the distance value: "))

firstOrd = ord(' ')
lastOrd = ord('~')
eTxt = ""
for char in txt:
    charOrd = ord(char)
    eOrd = charOrd - dist
    if eOrd < firstOrd:
        eOrd = lastOrd - firstOrd - charOrd
    eTxt += chr(eOrd)

print(eTxt)