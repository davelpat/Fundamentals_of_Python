"""
File: paneldemoversion1.py
A complex layout without nested frames.
"""

from breezypythongui import EasyFrame

class PanelDemo(EasyFrame):

    def __init__(self):

        # Create the main frame
        EasyFrame.__init__(self, "Panel Demo - v1")
        
        # Create and add widgets to the window
        self.addLabel(text = "Label 1", row = 0, column = 0)
        self.addTextField(text = "Text1", row = 0, column = 1,
                          columnspan = 2)
        self.addLabel(text = "Label 2", row = 1, column = 0)
        self.addTextField(text = "Text2", row = 1, column = 1,
                          columnspan = 2)

        # Create and add buttons to the window
        self.addButton(text = "B1", row = 2, column = 0)
        self.addButton(text = "B2", row = 2, column = 1)
        self.addButton(text = "B3", row = 2, column = 2)

def main():
    """Instantiate and pop up the window."""
    PanelDemo().mainloop()

if __name__ == "__main__":
    main()
