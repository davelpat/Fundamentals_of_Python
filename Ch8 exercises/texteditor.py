"""
Instructions for programming Exercise 8.8

Write a GUI-based program that allows the user to open, edit, and save text
files. The GUI should include a labeled entry field for the filename and a
multiline text widget for the text of the file. The user should be able to
scroll through the text by manipulating a vertical scrollbar. Include command
buttons labeled Open, Save, and New that allow the user to open, save, and
create new files. The New command should then clear the text widget and the
entry widget.
"""

"""
File: texteditor.py
Project 8.8
"""

from breezypythongui import EasyFrame
import tkinter.filedialog


class TextEditor(EasyFrame):
    """Demonstrates the use of a file dialog."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, "Text Editor")
        self.file_name = ""

        self.outputArea = self.addTextArea("", row=0, column=0, columnspan=3,
                                           width=80, height=15)
        self.newButton = self.addButton(text="New", row=1, column=0,
                                        command=self.newFile)
        self.openButton = self.addButton(text="Open", row=1, column=1,
                                         command=self.openFile)
        self.saveButton = self.addButton(text="Save", row=1, column=2,
                                         command=self.saveFile)

    # Event handling methods.
    def newFile(self):
        """Clears the text area and the title bar."""
        self.outputArea.setText("")
        self.file_name = ""
        self.setTitle("")

    def openFile(self):
        """Pops up an open file dialog, and if a file is
        selected, displays its text in the text area and
        its pathname in the title bar."""
        fList = [("Text files", "*.txt")]
        self.file_name = tkinter.filedialog.askopenfilename(parent=self,
                                                            filetypes=fList)
        if self.file_name != "":
            file = open(self.file_name, 'rt')
            text = file.read()
            file.close()
            self.outputArea.setText(text)
            self.setTitle(self.file_name)

    def saveFile(self):
        """Pops up an open file dialog, and saves
        the contents of the text area to the selected
        file name."""
        # tmp = self.title["text"]
        # self.outputArea.appendText("\ntitle is "+tmp)
        text = self.outputArea.getText()
        if self.file_name == "":
            fList = [("Text files", "*.txt")]
            file = tkinter.filedialog.asksaveasfile(parent=self,
                                                    filetypes=fList)
            self.file_name = file.name
        else:
            file = open(self.file_name, 'wt')

        file.write(text)
        file.close()
        self.setTitle(self.file_name)


def main():
    """Instantiate and pop up the window."""
    TextEditor().mainloop()


if __name__ == "__main__":
    main()
