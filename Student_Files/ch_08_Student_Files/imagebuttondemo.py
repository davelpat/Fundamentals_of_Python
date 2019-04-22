"""
File: imagebuttondemo.py
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

class ImageButtonDemo(EasyFrame):
    """Displays an image button and a caption."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Image Button Demo")
        self.setResizable(False)

        # Add the labels to the window.
        imageButton = self.addButton(text = "",
                                   row = 0, column = 0,
                                     command = self.smokey)
        textLabel = self.addLabel(text = "Smokey the cat",
                                  row = 1, column = 0,
                                  sticky = "NSEW")
        
        # Load the image and associate it with the image label.
        self.image = PhotoImage(file = "smokey.gif")
        imageButton["image"] = self.image

        # Set the font and color of the caption.
        font = Font(family = "Verdana", size = 20, slant = "italic")
        textLabel["font"] = font
        textLabel["foreground"] = "blue"

    def smokey(self):
        self.messageBox(message = "Hi, I'm Smokey!")

def main():
    """Instantiates and pops up the window."""
    ImageButtonDemo().mainloop()

if __name__ == "__main__":
    main()
