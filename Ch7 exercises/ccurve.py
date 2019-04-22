"""
Program file: ccurve.puy
Author: Ken
This program prompts the user for the level of a c-curve
and draws the c-curve of that level.
"""

from turtle import Turtle, tracer, update
import random



def cCurve(t, x1, y1, x2, y2, level, colors_list):
    """Draws a c-curve of the given level."""

    def drawLine(x1, y1, x2, y2):
        """Draws a line segment between the endpoints."""
        t.up()
        t.goto(x1, y1)
        t.down()
        t.goto(x2, y2)

    t.pencolor(random.choice(colors_list))

    if level == 0:
        drawLine(x1, y1, x2, y2)
    else:
        xm = (x1 + x2 + y1 - y2) // 2
        ym = (x2 + y1 + y2 - x1) // 2
        cCurve(t, x1, y1, xm, ym, level - 1, colors_list)
        cCurve(t, xm, ym, x2, y2, level - 1, colors_list)


def get_color_list(colors_file="colors_list.txt"):
    colors_list = []
    f = open(colors_file, 'r')
    for line in f:
        colors_list += line.split()
    return colors_list


def main():
    level = int(input("Enter the level (0 or greater): "))
    # colors_file = input("Enter the colors list filename: ")

    t = Turtle()
    if level > 8:
        tracer(False)
    t.hideturtle()
    cCurve(t, 50, -50, 50, 50, level, get_color_list())
    if level > 8:
        update()

    # Added to prevent the program from exiting and clearing the image
    done = input("Enter to exit: ")


if __name__ == '__main__':
    main()
