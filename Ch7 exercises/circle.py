from turtle import Turtle, tracer, update
import math


def drawCircle(t, x, y, radius, segments = 120):
    """Draws a circle of the given radius at with the center at the given point."""

    # get to the circumference
    t.up()
    t.goto(x + radius, y)
    t.setheading(90)

    # segment length
    seg_len = 2 * math.pi * radius / segments
    angle = 360 / segments

    tracer(False)

    # draw the circle
    t.down()
    for seg in range(segments):
        t.forward(seg_len)
        t.left(angle)

    update()


def main():
    # (x, y) = input("Enter the x and y coordinates of the circle's center: ").split()
    # radius = input("Enter the circle's radius: ")
    # (x, y, radius) = map(int, [x, y, radius])
    t = Turtle()
    # t.pencolor("blue")
    # t.hideturtle()

    # drawCircle(t, x, y, radius)
    drawCircle(t, 25, 75, 100)

    input("Enter <return> to exit")



if __name__ == '__main__':
    main()
