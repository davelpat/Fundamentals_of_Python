"""
Instructions for programming Exercise 4.4

Octal numbers have a base of eight and the digits 0–7. Write the scripts octalToDecimal.py and decimalToOctal.py, which convert numbers between the octal and decimal representations of integers.

These scripts use algorithms that are similar to those of the binaryToDecimal and decimalToBinary scripts developed in the Section: Strings and Number Systems.

An example of octalToDecimal.py input and output is shown below:

Enter a string of octal digits: 234

The integer value is 156
An example of decimalToOctal.py input and output is shown below:

Enter a decimal integer: 27

Quotient Remainder Octal
    3       3           3
    0       3          33
The octal representation is 33
"""

"""
File: octaltodecimal.py
Converts a string of octal numbers to a decimal integer.
"""

ostring = input("Enter an octal number: ")
decimal = 0
exponent = len(ostring) - 1
for digit in ostring:
    decimal += int(digit) * 8 ** exponent
    exponent = exponent - 1
print("The integer value is", decimal)