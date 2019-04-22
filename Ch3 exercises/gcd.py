""" Instructions

The greatest common divisor of two positive integers, A and B, is the largest
number that can be evenly divided into both of them. Euclid’s algorithm can be
used to find the greatest common divisor (GCD) of two positive integers. You can
use this algorithm in the following manner:

Compute the remainder of dividing the larger number by the smaller number.
Replace the larger number with the smaller number and the smaller number with
the remainder. Repeat this process until the smaller number is zero.

The larger number at this point is the GCD of A and B. Write a program that lets
the user enter two integers and then prints each step in the process of using
the Euclidean algorithm to find their GCD.

An example of the program input and output is shown below:

Enter the smaller number: 5 Enter the larger number: 15

The greatest common divisor is 5
"""

smaller = int(input("Enter the smaller integer: "))
larger = int(input("Enter the larger integer: "))

while True:
    rem = larger % smaller
    if rem == 0:
        print("The greatest common divisor is", smaller)
        break
    larger = smaller
    smaller = rem
