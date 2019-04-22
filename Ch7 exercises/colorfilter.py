"""
File: colorfilter.py
Project 7.9

Defines and tests a function for color filtering.  Uses this
function to define functions for lightening and darkening images.
"""

from images import Image


# from operator import add

def colorFilter(image, rgbTriple):
    """Adds the given rgb values to each pixel after normalizing."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            image.setPixel(x, y, adjust_pixel(image.getPixel(x, y), rgbTriple))


def adjust_pixel(pixel, rgb_adjustment):
    """Adjusts a pixel by amount and constrains pixel elements to the range of 0 <= pixel <= 255"""
    colors = list(pixel)
    adjustment = list(rgb_adjustment)
    for rgb in range(3):
        colors[rgb] += adjustment[rgb]
        if colors[rgb] < 0:
            colors[rgb] = 0
        elif colors[rgb] > 255:
            colors[rgb] = 255
    return tuple(colors)


def lighten(image, amount):
    """Lightens image by amount."""
    rgb_adjustment = (amount, amount, amount)
    colorFilter(image, rgb_adjustment)


def darken(image, amount):
    """Darkens image by amount."""
    rgb_adjustment = (-amount, -amount, -amount)
    colorFilter(image, rgb_adjustment)


def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    # lighten(image, 50) #Edit this line to test different functions and perameters.
    colorFilter(image, (50, 0, 0))
    image.draw()


if __name__ == "__main__":
    main()
