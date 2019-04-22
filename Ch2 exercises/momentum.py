"""
An object’s momentum is its mass multiplied by its velocity.

Write a program that accepts an object’s mass (in kilograms) and velocity (in meters per second) as inputs,
and then outputs its momentum.

The kinetic energy of a moving object is given by the formula KE = ½mv2
where m is the object’s mass and v is its velocity.

Modify the program you created in Project 5 so that it prints the object’s kinetic energy as well as its momentum.

Below is an example of the progam input and output:

Mass: 5
Velocity: 2.5

The object's momentum is 12.5
The object's kinetic energy is 15.625
"""

# Request the input
mass = float(input("Enter the object's mass: "))
velocity = float(input("Enter the object's velocity: "))

# Compute the momentum
momentum = mass * velocity

# Compute the kinetic energy
kineticEnergy = 0.5 * mass * velocity ** 2

# Display the results
print("The object's momentum is", momentum)
print("The object's kinetic energy is", kineticEnergy)
