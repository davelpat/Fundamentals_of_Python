"""
File: filedialogdemo.py
"""

from breezypythongui import EasyFrame
import tkinter.filedialog

class FileDialogDemo(EasyFrame):
    """Demonstrates the use of a file dialog."""
    
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, "File Dialog Demo")
        self.outputArea = self.addTextArea("", row = 0, column = 0,
                                           width = 80, height = 15)
        self.addButton(text = "Open", row = 1, column = 0,
                       command = self.openFile)

    # Event handling method.
    def openFile(self):
        """Pops up an open file dialog, and if a file is
        selected, displays its text in the text area and
        its pathname in the title bar."""
        fList = [("Python files", "*.py"), ("Text files", "*.txt")]
        fileName = tkinter.filedialog.askopenfilename(parent = self,
                                                      filetypes = fList)
        if fileName != "":
            file = open(fileName, 'r')
            text = file.read()
            file.close()
            self.outputArea.setText(text)
            self.setTitle(fileName)

def main():
    """Instantiate and pop up the window."""
    FileDialogDemo().mainloop()

if __name__ == "__main__":
 main()
   
