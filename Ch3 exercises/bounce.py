"""
Instructions

A standard science experiment is to drop a ball and see how high it bounces.
Once the “bounciness” of the ball has been determined, the ratio gives a
bounciness index.

For example, if a ball dropped from a height of 10 feet bounces 6 feet high, the
index is 0.6, and the total distance traveled by the ball is 16 feet after one
bounce. If the ball were to continue bouncing, the distance after two bounces
would be 10 ft + 6 ft +6 ft + 3.6 ft = 25.6 ft. Note that the distance traveled
for each successive bounce is the distance to the floor plus 0.6 of that
distance as the ball comes back up.

Write a program that lets the user enter the initial height from which the ball
is dropped, the bounciness index, and the number of times the ball is allowed to
continue bouncing. Output should be the total distance traveled by the ball.

Below is an example of the program input and output:

Enter the height from which the ball is dropped: 25
Enter the bounciness index of the ball: .5
Enter the number of times the ball is allowed to continue bouncing: 3

Total distance traveled is: 65.625 units.
"""

# get the input parameters
height = initialHeight = float(input("Enter the height from which the ball is dropped: "))
ratio = float(input("Enter the bounciness index of the ball: "))
numBounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))
# numBounces assumes that the ball is caught at the top of the last bounce
# print("height =", height, "ratio =", ratio, "numbounces =", numBounces)

distance = 0.0
for bounce in range(0, numBounces):
    bounceHeight = height * ratio
    distance += height + bounceHeight
    height = bounceHeight
    # print("Interation =", bounce, "bounceHeight =", bounceHeight, "distance =", distance, "new height =", height)

print("Total distance traveled is:", distance, "units.")
