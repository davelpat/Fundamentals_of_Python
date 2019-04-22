"""
File: prompterboxdemo.py
"""

from breezypythongui import EasyFrame

class PrompterBoxDemo(EasyFrame):
    """Demonstrates the use of prompter boxes."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Prompter Box Demo",
                           width = 300, height = 100)
        self.label = self.addLabel(text = "", row = 0, column = 0,
                                   sticky = "NSEW")
        
        self.addButton(text = "Username",row = 1, column = 0,
                       command = self.getUserName)

    def getUserName(self):
        text = self.prompterBox(title = "Input Dialog",
                                promptString = "Your username:")
        self.label["text"] = "Hi, " + text + "!"

def main():
    """Instantiate and pop up the window."""
    PrompterBoxDemo().mainloop()

if __name__ == "__main__":
    main()


