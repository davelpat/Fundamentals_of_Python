"""
File: sharpen.py
Project 7.10

Defines and tests a function to sharpen an image.
"""

from images import Image


def sharpen(image, degree, threshold):
    """Builds and returns a sharpened image.  Expects an image
    and two integers (the degree to which the image should be sharpened and the
    threshold used to detect edges) as arguments."""

    new = image.clone()

    for y in range(image.getHeight() - 1):
        for x in range(1, image.getWidth()):
            old_pixel = image.getPixel(x, y)
            left_pixel = image.getPixel(x - 1, y)
            bottom_pixel = image.getPixel(x, y + 1)

            old_lum = average(old_pixel)
            left_lum = average(left_pixel)
            bottom_lum = average(bottom_pixel)

            if abs(old_lum - left_lum) > threshold or \
                    abs(old_lum - bottom_lum) > threshold:
                new.setPixel(x, y, darken_pixel(old_pixel, degree))

    return new


def average(triple):
    (r, g, b) = triple
    return (r + g + b) // 3


def darken_pixel(pixel, adjustment):
    """Darkens a pixel by amount and constrains pixel elements to the range of 0 <= pixel <= 255"""
    colors = list(pixel)
    for rgb in range(3):
        colors[rgb] -= adjustment
        if colors[rgb] < 0:
            colors[rgb] = 0
        elif colors[rgb] > 255:
            colors[rgb] = 255
    return tuple(colors)


def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    newimage = sharpen(image, 20, 15)
    newimage.draw()


if __name__ == "__main__":
    main()
