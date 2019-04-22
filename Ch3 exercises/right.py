"""
Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is a right
triangle.

Recall from the Pythagorean theorem that in a right triangle, the square of one
side equals the sum of the squares of the other two sides.

Use "The triangle is a right triangle." and "The triangle is not a right triangle."
as your final outputs.

An example of the program input and proper output format is shown below:

Enter the first side: 3
Enter the second side: 4
Enter the third side: 5

The triangle is a right triangle.
"""

# Get the side lengths
sideA = float(input("Enter length of side 1 of the triangele: "))
sideB = float(input("Enter length of side 2 of the triangele: "))
sideC = float(input("Enter length of side 3 of the triangele: "))

# Determine which side is potentially the hypotenuse
if sideA == max(sideA, sideB, sideC):
    hypot = sideA
    side2 = sideB
    side3 = sideC
elif sideB == max(sideA, sideB, sideC):
    hypot = sideB
    side2 = sideA
    side3 = sideC
else:
    hypot = sideC
    side2 = sideB
    side3 = sideA

# Determinei if it is a right triangle using the Pythagorean theorem
if hypot ** 2 == (side2 ** 2 + side3 ** 2):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
