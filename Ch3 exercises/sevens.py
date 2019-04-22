"""
Instructions

In the game of Lucky Sevens, the player rolls a pair of dice. If the dots add up
to 7, the player wins $4; otherwise, the player loses $1.

Suppose that, to entice the gullible, a casino tells players that there are lots
of ways to win: (1, 6), (2, 5), and so on. A little mathematical analysis
reveals that there are not enough ways to win to make the game worthwhile;
however, because many people’s eyes glaze over at the first mention of
mathematics, your challenge is to write a program that demonstrates the futility
of playing the game.

Your program should take as input the amount of money that the player wants to
put into the pot, and play the game until the pot is empty. At that point, the
program should print:

The number of rolls it took to break the player
The maximum amount of money in the pot.
An example of the program input and output is shown below:

How many dollars do you have? 50

You are broke after 220 rolls.
You should have quit after 6 rolls when you had $59.
"""

from random import randint

# Get the initial pot and initialize the roll count
max_pot = pot = int(input("How many dollars do you have? "))
max_pot_roll = num_rolls = 0

# Play the game
while pot > 0:
    # Roll two dice
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    num_rolls += 1

    # Win if sum = 7, worth $4, else lose 41
    if die1 + die2 == 7:
        pot += 4

        # keep track of best point to quit
        if pot > max_pot:
            max_pot = pot
            max_pot_roll = num_rolls
    else:
        pot -= 1

print("You are broke after", str(num_rolls), "rolls.")
print("You should have quit after", str(max_pot_roll), "rolls when you had $" + str(max_pot) + ".")
