"""
File: bouncywithgui.py
Project 8.2

Determines the distance traveled by a bouncing ball.

Inputs: Initial height, bounciness index, and number of bounces
numBounces assumes that the ball is caught at the top of the last bounce
"""

from breezypythongui import EasyFrame


def computeDistance(height, index, bounces):
    """Computes the total distance traveled by the ball,
    given an initial height, bounciness index, and
    number of bounces."""
    pass


class BouncyGUI(EasyFrame):

    def __init__(self):
        """Set up the window and widgets."""
        EasyFrame.__init__(self, title="Bouncy")

        # Label and field for the initial height
        self.addLabel(text="Initial Height",
                      row=0, column=0)
        self.heightField = self.addFloatField(value=0.0,
                                              row=0, column=1)

        # Label and field for the bounciness index
        self.addLabel(text="Bounciness Index",
                      row=1, column=0)
        self.indexField = self.addFloatField(value=0.0,
                                             row=1, column=1)

        # Label and field for the number of bounces
        self.addLabel(text="Number of bounces",
                      row=2, column=0)
        self.bouncesField = self.addIntegerField(value=0,
                                                 row=2, column=1)

        # The command button
        self.addButton(text="Compute distance",
                       row=3, column=0, columnspan=2,
                       command=self.computeDistance)

        # Label and field for the distance traveled
        self.addLabel(text="Distance traveled",
                      row=4, column=0)
        self.distanceField = self.addFloatField(value=0,
                                                row=4, column=1)

    def computeDistance(self):
        """
        Event handler for the Compute button and set the
        distanceField.
        """
        distance = 0.0
        height = self.heightField.getNumber()
        ratio = self.indexField.getNumber()
        numBounces = self.bouncesField.getNumber()

        for bounce in range(numBounces):
            bounceHeight = height * ratio
            distance += height + bounceHeight
            height = bounceHeight

        self.distanceField.setNumber(distance)


def main():
    """Instantiate and pop up the window."""
    BouncyGUI().mainloop()


if __name__ == "__main__":
    main()
