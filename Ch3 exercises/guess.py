"""
Modify the guessing-game program so that the user thinks of a number that the
computer must guess.

The computer must make no more than the minimum number of guesses, and it must
prevent the user from cheating by entering misleading hints.

Use "I'm out of guesses, and you cheated" and "Hooray, I've got it in X tries"
as your final output.

(Hint: Use the math.log function to compute the minimum number of guesses needed
after the lower and upper bounds are entered.)

Below are two test runs of the program:

Enter the smaller number: 0
Enter the larger number: 10

0 10
Your number is 5
Enter =, <, or >: <
0 4
Your number is 2
Enter =, <, or >: >
3 4
Your number is 3
Enter =, <, or >: =
Hooray, I've got it in 3 tries!

Enter the smaller number: 0
Enter the larger number: 50

0 50
Your number is 25
Enter =, <, or >: <
0 24
Your number is 12
Enter =, <, or >: <
0 11
Your number is 5
Enter =, <, or >: <
0 4
Your number is 2
Enter =, <, or >: <
0 1
Your number is 0
Enter =, <, or >: >
1 1
Your number is 1
Enter =, <, or >: >
I'm out of guesses, and you cheated!
"""

import math

# get the range
lower = int(input("Enter the smaller number: "))
upper = int(input("Enter the larger number: "))
rng = upper - lower + 1
# print("range =", rng)
idealMaxGuesses = round(math.log(rng, 2))

cnt = 0
while True:
    cnt += 1
    if cnt > idealMaxGuesses:
        print("I'm out of guesses, and you cheated!")
        break
    print(lower, upper)
    guess = int((lower + upper) // 2)
    print("Your number is", guess)
    feedback = input("Enter =, <, or >: ")
    if feedback == "=":
        print("Hooray, I've got it in", cnt, "tries!")
        break
    elif feedback == "<":
        upper = guess - 1
    else:
        lower = guess + 1
