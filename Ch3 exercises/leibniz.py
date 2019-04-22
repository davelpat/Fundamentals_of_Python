"""
Instructions

The German mathematician Gottfried Leibniz developed the following method to
approximate the value of π:

π/4 = 1 - 1/3 + 1/5 - 1/7 + . . .

Write a program that allows the user to specify the number of iterations used in
this approximation and that displays the resulting value.

An example of the program input and output is shown below:

Enter the number of iterations: 5

The approximation of pi is 3.3396825396825403
"""

reps = int(input("Enter the number of iterations: "))
est = float(0)
sign = 1

for denom in range(1, reps * 2, 2):
    # print("denom =", denom, end="")
    est = est + sign / denom
    # print(" estimate =", est * 4)
    sign *= -1

print("pi estimate after", reps, "iteratons is", est * 4)