"""
File: enlarge.py
Project 7.11

Defines and tests a function to enlarge an image.
"""

from images import Image


def enlarge(image, factor):
    """Builds and returns a copy of the image which is larger
    by the factor."""

    def block_copy_pixel_to(image, row_index, line, pixel_to_copy, factor):
        for x in range(factor):
            for y in range(factor):
                image.setPixel(row_index + x, line + y, pixel_to_copy)

    old_height = image.getHeight()
    old_width = image.getWidth()
    new_height = old_height * factor
    new_width = old_width * factor

    new_image = Image(new_width, new_height)

    nhi = 0  # new height index
    for ohi in range(old_height):  # original image height index
        # new left & right indices
        nli = 0
        nri = new_width - 1
        # original left & right indices
        oli = 0
        ori = old_width - 1

        # Copy blocks of the same pixel to the new image
        while oli < ori:
            old_left_pixel = image.getPixel(oli, ohi)
            block_copy_pixel_to(new_image, nli, nhi, old_left_pixel, factor)
            old_right_pixel = image.getPixel(ori, ohi)
            block_copy_pixel_to(new_image, nri - factor, nhi, old_right_pixel, factor)

            # Increment the image indices
            nli += factor
            nri -= factor

            oli += 1
            ori -= 1

        # increment new image row index
        nhi += factor

    return new_image


def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    newimage = enlarge(image, 2)
    newimage.draw()


if __name__ == "__main__":
    main()
