"""
Instructions

Write a GUI-based program that implements an image browser for your computer’s
file system. The look, feel, and program logic should be like those of the
simple text file browser developed in this chapter. The file dialog should filter
for GIF image files, and create and open a PhotoImage when a file is accessed.
"""

"""
File: imagebrowser.py
Project 8.9

Browser for image (.gif) files.
"""

from breezypythongui import EasyFrame, EasyCanvas
from tkinter import PhotoImage
import tkinter.filedialog


class ImageBrowser(EasyFrame):

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title="Image Browser")

        self.imageLabel = self.addLabel("", row=0, roww
                                        column=0,
                                        sticky="NSEW")

        self.findImageButton = self.addButton(text="Find Image",
                                              row=1, column=0,
                                              command=self.findImage)

    def findImage(self):
        """Pops up an open file dialog, and if a file is
        selected, displays its image in the label and
        its pathname in the title bar."""

        # Request the file name
        fList = [("Image files", "*.gif")]
        self.fileName = tkinter.filedialog.askopenfilename(parent=self,
                                                           filetypes=fList)

        if self.fileName != "":
            self.setTitle(self.fileName)
            self.image = PhotoImage(file=self.fileName)
            self.imageLabel["image"] = self.image


def main():
    """Instantiate and pop up the window."""
    ImageBrowser().mainloop()


if __name__ == "__main__":
    main()
