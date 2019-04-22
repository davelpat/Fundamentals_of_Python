from breezypythongui import EasyFrame


# other imports


class CounterDemo(EasyFrame):

    def __init__(self):
        """Sets up the window"""
        EasyFrame.__init__(self, title="Counter Demo")
        self.setSize(200, 75)

        # Instance variable to track the count
        self.count = 0

        # Label to display the count
        # I assume a text field is not being used to avoid the field boundary
        self.label = self.addLabel(text="0",
                                   row=0, column=0,
                                   sticky="NSEW",
                                   columnspan=2)

        # Two command buttons
        self.addButton(text="Next",
                       row=1, column=0,
                       command=self.next)

        self.addButton(text="Reset",
                       row=1, column=1,
                       command=self.reset)

    # Event handlers
    def next(self):
        """Increments the count and updates the display"""
        self.count += 1
        self.label["text"] = str(self.count)

    def reset(self):
        """Ressets the count to 0 and updates the display"""
        self.count = 0
        self.label["text"] = str(self.count)


def main():
    """Instantiates and pops up the window"""
    CounterDemo().mainloop()


if __name__ == '__main__':
    main()
