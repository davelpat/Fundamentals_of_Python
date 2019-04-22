from breezypythongui import EasyFrame

# other imports


class ApplicationName(EasyFrame):

    def __init__(self):
        """Sets up the window, labels, and buttons"""
        EasyFrame.__init__(self)
        # other code for window components, e.g. self.addLabel(...)

    # Other methods to handle events


def main():
    """Instantiates and pops up the window"""
    ApplicationName().mainloop()


if __name__ == '__main__':
    main()
