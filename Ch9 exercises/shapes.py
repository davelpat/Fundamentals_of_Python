"""
File: shapes.py
Project 9.10

Defines classes for line segments, circles, and rectangles using a turtle
object to draw them.

"""

import math


class Shape(object):
    """Represents a shape with a color and a turtle."""

    def __init__(self, turtle, color):
        self.turtle = turtle
        self.color = color

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color


class Line(Shape):
    """Represents a line segment."""

    def __init__(self, x1, y1, x2, y2, turtle, color):
        Shape.__init__(self, turtle, color)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def draw(self):
        """Draws a line."""
        (r, g, b) = self.color
        self.turtle.up()
        self.turtle.goto(self.x1, self.y1)
        self.turtle.pencolor(r, g, b)
        self.turtle.down()
        self.turtle.goto(self.x2, self.y2)


class Circle(Shape):
    """Represents a circle."""

    def __init__(self, x, y, radius, turtle, color):
        Shape.__init__(self, turtle, color)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        """Draws a circle."""
        (r, g, b) = self.color
        amount = 2.0 * math.pi * self.radius / 120.0
        self.turtle.up()
        self.turtle.goto(self.x + self.radius, self.y)
        self.turtle.setheading(90)
        self.turtle.down()
        self.turtle.pencolor(r, g, b)
        for count in range(120):
            self.turtle.left(3)
            self.turtle.forward(amount)


class Rectangle(Shape):
    """Represents a rectangle."""

    def __init__(self, x, y, width, height, turtle, color):
        Shape.__init__(self, turtle, color)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        """Draws a rectangle."""
        (r, g, b) = self.color
        self.turtle.up()
        self.turtle.goto(self.x, self.y)
        self.turtle.setheading(0)
        self.turtle.down()
        self.turtle.pencolor(r, g, b)
        self.turtle.forward(self.width)
        self.turtle.left(-90)
        self.turtle.forward(self.height)
        self.turtle.left(-90)
        self.turtle.forward(self.width)
        self.turtle.left(-90)
        self.turtle.forward(self.height)

