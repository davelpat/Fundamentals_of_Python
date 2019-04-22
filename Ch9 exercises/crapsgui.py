"""
Instructions for programming Exercise 9.7

Convert the DiceDemo program discussed in this chapter to a completed craps game
application, using the Player data model class you developed in Project 6.
"""

"""
File: dicedemo.py

Pops up a window that allows the user to roll the dice.
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from die import Die


class CrapsGUI(EasyFrame):

    def __init__(self):
        """Creates the dice, and sets up the Images and labels
        for the two dice to be displayed, the state label,
        and the two command buttons."""
        EasyFrame.__init__(self, title="Craps Game")
        # self.setSize(270, 200)
        self.die1 = Die()
        self.die2 = Die()
        self.rolls = []

        self.dieLabel1 = self.addLabel("", row=0,
                                       column=0,
                                       sticky="NSEW")
        self.dieLabel2 = self.addLabel("", row=0,
                                       column=1,
                                       sticky="NSEW")
        # self.stateLabel = self.addLabel("", row=1, column=0,
        #                                 sticky="NSEW",
        #                                 columnspan=2)
        # self.summary = self.addLabel("", row=1, column=0,
        #                              sticky="W",
        #                              columnspan=2)

        self.stateArea = self.addTextArea("",
                                          row=1, column=0,
                                          width=40, height=10)

        self.rollButton = self.addButton(row=2, column=0,
                                         text="Roll",
                                         command=self.nextRoll)
        self.gameButton = self.addButton(row=2, column=1,
                                         text="New game",
                                         command=self.newGame)
        # self.summary_button = self.addButton(row=2, column=2,
        #                                   text="Game summary",
        #                                   command=self.game_summary)
        self.refreshImages()

    def __str__(self):
        """Returns a string representation of the list of rolls."""
        # result = "Game summary:\n"
        for (v1, v2) in self.rolls:
            result = result + str((v1, v2)) + " " + \
                     str(v1 + v2) + "\n"
        return result

    # def game_summary(self):
    #     # self.summary_label["text"] = "Game summary:\n" + self.__str__()
    #     self.summary["text"] = str(self)

    def getNumberOfRolls(self):
        """Returns the number of the rolls."""
        return len(self.rolls)

    def check_win(self, roll_total):
        """Checks if the current roll is a winner
        :param roll_total:
        """

        # Is it the first roll?
        if self.getNumberOfRolls() == 1:
            self.first_roll = roll_total
            if roll_total in (2, 3, 12):
                self.update_state("lost", roll_total)
            elif roll_total in (7, 11):
                self.update_state("won", roll_total)
            else:
                self.update_state("reroll", roll_total)
        else:
            if roll_total == 7:
                self.update_state("lost", roll_total)
            elif roll_total == self.first_roll:
                self.update_state("won", roll_total)
            else:
                self.update_state("reroll", roll_total)

    def nextRoll(self):
        """Rolls the dice and updates the view with
        the results."""
        self.die1.roll()
        self.die2.roll()
        (v1, v2) = (self.die1.getValue(),
                    self.die2.getValue())
        self.rolls.append((v1, v2))
        self.check_win(v1 + v2)
        self.refreshImages()

    def update_state(self, state, roll_total):
        self.stateArea.appendText("Total = " + str(roll_total) + "\n")
        if state == "lost":
            # self.stateLabel["text"] = "You lose on " + str(roll_total)
            self.stateArea.appendText("You lose!" + "\n")
            self.rollButton["state"] = "disabled"
        elif state == "won":
            # self.stateLabel["text"] = "You win with " + str(roll_total)
            self.stateArea.appendText("You win!" + "\n")
            self.rollButton["state"] = "disabled"

    def newGame(self):
        """Create a new craps game and updates the view."""
        self.die1 = Die()
        self.die2 = Die()
        self.rolls = []
        # self.stateLabel["text"] = ""
        # self.summary["text"] = ""
        self.stateArea.setText("")
        self.rollButton["state"] = "normal"
        self.refreshImages()

    def refreshImages(self):
        """Updates the images in the window."""
        fileName1 = "DICE/" + str(self.die1) + ".gif"
        fileName2 = "DICE/" + str(self.die2) + ".gif"
        self.image1 = PhotoImage(file=fileName1)
        self.dieLabel1["image"] = self.image1
        self.image2 = PhotoImage(file=fileName2)
        self.dieLabel2["image"] = self.image2


def main():
    CrapsGUI().mainloop()


if __name__ == "__main__":
    main()
