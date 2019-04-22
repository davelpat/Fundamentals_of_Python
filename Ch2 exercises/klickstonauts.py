"""
Write a program that takes as input a number of kilometers and prints the corresponding number of nautical miles.

Use the following approximations:

A kilometer represents 1/10,000 of the distance between the North Pole and the equator.
There are 90 degrees, containing 60 minutes of arc each, between the North Pole and the equator.
A nautical mile is 1 minute of an arc.
An example of the program input and output is shown below:

Enter the number of kilometers: 100
The number of nautical miles is 54
"""

# Kilometers between North Pole and Equator
kilosPerArc = 10000

# Minutes between North Pole and Equator
minutesPerArc = 90 * 60

# Ratio of nautical miles per kilometer
nmPerKm = minutesPerArc / kilosPerArc

kilometers = float(input("Enter the number of kilometers: "))
print("The number of nautical miles is", kilometers * nmPerKm)
