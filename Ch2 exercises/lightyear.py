"""
Light travels at 3 × 108 meters per second. A light-year is the distance a light beam travels in one year.

Write a program that calculates and displays the value of a light-year.

Useful facts:

Seconds in a year = 365×24×602
Rate = 3×108 meters per second
Below is an example of the correct output format:

Light travels X meters in a year.
"""

# Seconds in a year
secs = 365*24*60**2
# Speed of light in m/s
rate = 3*10**8

print("Light travels", rate * secs , "meters in a year.")
