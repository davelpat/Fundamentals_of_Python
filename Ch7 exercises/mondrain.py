"""
The twentieth-century Dutch artist Piet Mondrian developed a style of abstract painting that exhibited simple
recursive patterns. To generate such a pattern with a computer, one would begin with a filled rectangle in a
random color and then repeatedly fill two unequal subdivisions with random colors.

The algorithm continues the process of subdivision until an “aesthetically right moment” is reached.
"""

from turtle import Turtle, tracer, update
from random import choice, random

COLORS = ["white"] * 5 + ["black"] * 2 + ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "grey"]


def draw_rectangles(t, corners, splits):
    def choose_ratio():
        denom = choice([3, 4, 5])
        if denom == 5:
            num = choice([1, 2])
        else:
            num = 1
        return round(num / denom, 2)

    def fill_rectangle(t, corners):
        (x1, y1) = corners[0]
        (x2, y2) = corners[1]

        t.fillcolor(choice(COLORS))

        t.up()
        t.goto(corners[0])

        t.begin_fill()
        t.down()
        t.goto((x1, y2))
        t.goto(corners[1])
        t.goto((x2, y1))
        t.goto(corners[0])
        t.end_fill()

    def split_rectangle(corners, ratio):
        """Takes the diagonal points of a rectangle and splits it into 2
           along the largest dimension using the given ratio"""
        (x1, y1) = corners[0]
        (x2, y2) = corners[1]
        # print("x1 = %i, y1 = %i, x2 = %i, y2 = %i, ratio = %f" % (x1, y1, x2, y2, ratio))
        xlen = x2 - x1
        ylen = y2 - y1

        # split the longest side most of the time
        if xlen >= ylen and random() >= 0.4:
            xm = x1 + round(xlen * ratio)
            return [(x1, y1), (xm, y2)], [(xm, y1), (x2, y2)]
        else:
            ym = y1 + round(ylen * ratio)
            return [(x1, y1), (x2, ym)], [(x1, ym), (x2, y2)]

    # Pick the ratios
    ratio = choose_ratio()

    if splits == 0:
        fill_rectangle(t, corners)
    else:
        # Split the rectangle -- maybe
        smaller_rect, larger_rect = split_rectangle(corners, ratio)
        # print("smaller_rect = [", smaller_rect[0], ",", smaller_rect[1],
        #       "], larger_rect = [", larger_rect[0], ",", larger_rect[1], "]")

        draw_rectangles(t, smaller_rect, splits - 1)
        draw_rectangles(t, larger_rect, splits - 1)


def main():
    # Get the size of the rectangle
    length, width = map(int, list(input("Enter size of rectangle: ").split()))
    corners = [(-length // 2, -width // 2), (length // 2, width // 2)]

    # How many iterations?
    splits = int(input("Enter number of splits: "))

    # Set up the turtle
    t = Turtle()
    t.hideturtle()
    pw = choice([3, 5, 7])
    t.pensize(pw)

    # Draw the rectangles
    draw_rectangles(t, corners, splits)

    input("Enter to exit")


if __name__ == '__main__':
    main()
