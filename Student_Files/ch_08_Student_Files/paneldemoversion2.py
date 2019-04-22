"""
File: paneldemoversion2.py
A complex layout with two panels representing nested frames.
"""

from breezypythongui import EasyFrame

class PanelDemo(EasyFrame):

    def __init__(self):

        # Create the main frame
        EasyFrame.__init__(self, "Panel Demo - v2")
        
        # Create the panel for the data
        dataPanel = self.addPanel(row = 0, column = 0,
                                  background = "gray")

        # Create and add widgets to the data panel
        dataPanel.addLabel(text = "Label 1", row = 0, column = 0,
                           background = "gray")
        dataPanel.addTextField(text = "Text1", row = 0, column = 1)
        dataPanel.addLabel(text = "Label 2", row = 1, column = 0,
                           background = "gray")
        dataPanel.addTextField(text = "Text2", row = 1, column = 1,)

        # Create the nested frame for the button panel
        buttonPanel = self.addPanel(row = 1, column = 0,
                                    background = "black")

        # Create and add buttons to the button panel
        buttonPanel.addButton(text = "B1", row = 0, column = 0)
        buttonPanel.addButton(text = "B2", row = 0, column = 1)
        buttonPanel.addButton(text = "B3", row = 0, column = 2)

def main():
    """Instantiate and pop up the window."""
    PanelDemo().mainloop()

if __name__ == "__main__":
    main()
