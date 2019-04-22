"""
Write a program that accepts the lengths of three sides of a triangle as inputs.

The program output should indicate whether or not the triangle is an equilateral triangle.

Use The triangle is equilateral. and The triangle is not equilateral. as your final
outputs.

An example of the program inputs and output is shown below:

Enter the first side: 2
Enter the second side: 2
Enter the third side: 2

The triangle is equilateral.
"""

# get the sides
sideA = float(input("Enter length of side 1 of the triangele: "))
sideB = float(input("Enter length of side 2 of the triangele: "))
sideC = float(input("Enter length of side 3 of the triangele: "))

# see if theya re all equal
if sideA == sideB and sideB == sideC:
	print("The triangle is equilateral.")
else:
	print("The triangle is not equilateral.")
