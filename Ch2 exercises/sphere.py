"""
Write a program that takes the radius of a sphere (a floating-point number) as input and then outputs the sphere’s:

Diameter (2 × radius)
Circumference (diameter × π)
Surface area (4 × π × radius × radius)
Volume (4/3 × π × radius × radius × radius)
Below is an example of the program input and output:

Radius = 5

Diameter     : 10.0
Circumference: 31.41592653589793
Surface area : 314.1592653589793
Volume       : 523.5987755982989
"""

import math

radius = float(input("Enter the sphere's radius: "))

print("Radius =", radius)
print("Diameter     :", radius * 2)
print("Circumference:", radius * 2 * math.pi)
print("Surface area :", 4 * math.pi * radius ** 2)
print("Volume       :", 4 / 3 * math.pi * radius ** 3)
