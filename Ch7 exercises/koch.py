"""
Author: Dave
Creation date: 2018-08-24

At the top level, the script uses a function drawFractalLine to draw three fractal lines.
Each line is specified by a given distance, direction (angle), and level.
The initial angles are 0, -120, and 120 degrees.

The function drawFractalLine is recursive.
If the level is 0, then the turtle moves the given distance in the given direction.
Otherwise, the function draws four fractal lines with ⅓ of the given distance,
angles that produce the given effect, and the given level minus 1.

Width = 200
Height = 200
Size = 150
Level = 4
"""

from turtle import Turtle, tracer, update

def drawFractalLine(t, distance, angle, level):

    def koch(t, distance, level):
        if level > 0:
            for angle in [60, -120, 60, 0]:
                koch(t, distance / 3, level - 1)
                t.left(angle)
        else:
            t.forward(distance)

    t.down()
    t.left(angle)
    koch(t, distance, level)


def main():
    t = Turtle()
    # t.up()
    # t.goto(50, 50)
    # t.down()
    t.setheading(180)  # West
    t.hideturtle()

    distance = 150
    level = 1

    if level >= 3:
        tracer(False)

    drawFractalLine(t, distance, 0, level)
    drawFractalLine(t, distance, -120, level)
    drawFractalLine(t, distance, -120, level)

    update()

    input("Enter to quit")

if __name__ == '__main__':
    main()
