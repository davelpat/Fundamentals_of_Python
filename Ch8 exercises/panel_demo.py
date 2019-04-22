from breezypythongui import EasyFrame


# other imports


class PanelDemo(EasyFrame):

    def __init__(self):
        """Sets up the window, labels, and buttons"""

        # Create the main frame
        EasyFrame.__init__(self, "Panel Demo - v2")

        # Create the nested frame for the date panel
        data_panel = self.addPanel(row=0, column=0,
                                   background="gray")

        # Create and add widgets to the data panel
        data_panel.addLabel(text="Label 1", row=0, column=0,
                            background="gray")
        data_panel.addTextField(text="Text1", row=0, column=1)
        data_panel.addLabel(text="Label 2", row=1, column=0,
                            background="gray")
        data_panel.addTextField(text="Text2", row=1, column=1)

        # Create nested frame for button panel
        button_panel = self.addPanel(row=1, column=0,
                                     background="black")

        # Create and add buttons to the button panel
        button_panel.addButton(text="B1", row=0, column=0)
        button_panel.addButton(text="B2", row=0, column=1)
        button_panel.addButton(text="B3", row=0, column=2)

    # Other methods to handle events


def main():
    """Instantiates and pops up the window"""
    PanelDemo().mainloop()


if __name__ == '__main__':
    main()
