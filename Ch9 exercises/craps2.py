"""
Instructions for programming Exercise 9.6

The play method in the Player class of the craps game plays an entire game
without interaction with the user. Revise the Player class so that its user can
make individual rolls of the dice and view the results after each roll. The
Player class no longer accumulates a list of rolls, but saves the string
representation of each roll after it is made.

Add new methods rollDice, getNumberOfRolls, isWinner, and isLoser to the Player
class. The last three methods allow the user to obtain the number of rolls and
to determine whether there is a winner or a loser. The last two methods are
associated with new Boolean instance variables (winner and loser respectively).
Two other instance variables track the number of rolls and the string
representation of the most recent roll (rollsCount and roll). Another instance
variable (atStartup) tracks whether or not the first roll has occurred.

At instantiation, the roll, rollsCount, atStartup, winner, and loser variables
are set to their appropriate initial values. All game logic is now in the
rollDice method. This method rolls the dice once, updates the state of the
Player object, and returns a tuple of the values of the dice for that roll.
Include in the module the playOneGame and playManyGames functions, suitably
updated for the new interface to the Player class.

"""

"""
File: craps.py

This module studies and plays the game of craps.
"""

from die import Die


class Player(object):

    def __init__(self):
        """Has a pair of dice and an empty rolls list, as well as state variables."""
        self.atStartup = True
        self.winner = False
        self.loser = False
        self.die1 = Die()
        self.die2 = Die()
        self.roll = ()
        self.firstSum = 0
        self.rollCount = 0

    def __str__(self):
        """Returns a string representation of the most recent roll."""
        return "Roll " + str(self.rollCount) + ": " + str(self.roll) + "\n"

    def getNumberOfRolls(self):
        """Returns the number of the rolls."""
        return self.rollCount

    def isLoser(self, sum):
        if (sum in (2, 3, 12) and self.atStartup) or \
                (sum == 7 and not self.atStartup):
            return True
        else:
            return False

    def isWinner(self, sum):
        if (sum in (7, 11) and self.atStartup) or \
                (sum == self.firstSum and not self.atStartup):
            return True
        else:
            return False

    def rollDice(self):
        """Plays a game, saves the rolls for that game, 
        and returns True for a win and False for a loss."""
        v1, v2 = self.roll_and_record()
        sum = v1 + v2
        if self.atStartup:
            self.firstSum = sum
        return sum

    def roll_and_record(self):
        self.die1.roll()
        self.die2.roll()
        (v1, v2) = (self.die1.getValue(),
                    self.die2.getValue())
        self.roll = (v1, v2)
        self.rollCount += 1
        return v1, v2


def playGame(player):
    """Plays a single game and prints the results."""
    sum = player.rollDice()
    print(player)
    if player.isWinner(sum):
        print("You win!")
    elif player.isLoser(sum):
        print("You lose!")
    if player.atStartup:
        player.atStartup = False


def playManyGames(number):
    """Plays a number of games and prints statistics."""
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    player = Player()
    for count in range(number):
        hasWon = player.rollDice()
        rolls = player.getNumberOfRolls()
        if hasWon:
            wins += 1
            winRolls += rolls
        else:
            losses += 1
            lossRolls += rolls
    print("The total number of wins is", wins)
    print("The total number of losses is", losses)
    print("The average number of rolls per win is %0.2f" % \
          (winRolls / wins))
    print("The average number of rolls per loss is %0.2f" % \
          (lossRolls / losses))
    print("The winning percentage is %0.3f" % (wins / number))


def main():
    """Plays a number of games and prints statistics.
    number = int(input("Enter the number of games: "))
    playManyGames(number)
    """

    player = Player()
    while True:
        ans = input("Would you like to roll the dice? (ynq) ")
        if ans == "y":
            playGame(player)
        else:
            break



if __name__ == "__main__":
    main()
