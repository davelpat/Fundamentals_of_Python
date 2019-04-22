"""
Program: newton.py
Author: Ken
Compute the square root of a number.
Dave: Modified to loop until empty string is entered
1. The input is a number.
2. The outputs are the program's estimate of the square root
   using Newton's method of successive approximations, and
   Python's own estimate using math.sqrt.
"""

import math


def main():
    while True:
        # Receive the input number from the user
        x = input("Enter a positive number or enter/return to quit: ")

        # Stop asking when no number is entered
        if x == "":
            break
        else:
            x = float(x)

        # Output the result
        print("The program's estimate is", newton(x))
        print("Python's estimate is     ", math.sqrt(x))


def newton(x):
    # Initialize the tolerance and estimate
    tolerance = 0.000001
    estimate = 1.0

    # Perform the successive approximations
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            return estimate


if __name__ == '__main__':
    main()
