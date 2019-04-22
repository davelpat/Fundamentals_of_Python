"""
Instructions for programming Exercise 5.3

Modify the sentence-generator program so that it inputs its vocabulary from a
set of text files at startup. The filenames are nouns.txt, verbs. txt,
articles.txt, and prepositions.txt.

(Hint: Define a single new function, getWords. This function should expect a
filename as an argument. The function should open an input file with this name,
define a temporary list, read words from the file, and add them to the list. The
function should then convert the list to a tuple and return this tuple. Call the
function with an actual filename to initialize each of the four variables for
the vocabulary.)

An example of the program input and output is shown below:

Enter the number of sentences: 1

THE GIRL SAW THE BALL BY THE BALL
"""

"""
Instructions for programming Exercise 5.4

Make the following modifications to the original sentence-generator program:

The prepositional phrase is optional. (It can appear with a certain probability.)
A conjunction and a second independent clause are optional: The boy took a drink
and the girl played baseball.
An adjective is optional: The girl kicked the red ball with a sore foot.
You should add new variables for the sets of adjectives and conjunctions.

An example of the program input and output is shown below:

Enter the number of sentences: 3

A LITTLE BALL HIT A LITTLE GIRL
THE BOY HIT THE LITTLE BAT BY THE RED BOY
A RED BOY SAW A RED BOY 
"""

"""
Program: generator.py
Author: Ken
Modifications by: Dave
Generates and displays sentences using a simple grammar
and vocabulary.  Words are chosen at random.
"""

import random
from random import randint


def getWordsFrom(wordsFile):
    """Builds and returns a tuple of words from the requested file."""
    words = []
    fIn = open(wordsFile, 'r')
    for line in fIn:
        # tmp = line.split
        # words += tmp
        words += list(line.split())
    return tuple(words)


# Files containing words from these parts of speech
adjectives = getWordsFrom("adjectives.txt")
articles = getWordsFrom("articles.txt")
conjunctions = getWordsFrom("conjunctions.txt")
nouns = getWordsFrom("nouns.txt")
prepositions = getWordsFrom("prepositions.txt")
verbs = getWordsFrom("verbs.txt")


# Frequency will be 1 out of *Range
prepRange = range(3)
conjRange = range(4)
adjRange = range(3)


def sentence():
    """Builds and returns a sentence."""
    sent = nounPhrase() + " " + verbPhrase()
    if random.choice(conjRange) == 1:
        sent += " " + random.choice(conjunctions) + " " + \
                nounPhrase() + " " + verbPhrase()
    return sent

def nounPhrase():
    """Builds and returns a noun phrase."""
    phrase = random.choice(articles)
    if random.choice(adjRange) == 1:
        phrase += " " + random.choice(adjectives)
    phrase += " " + random.choice(nouns)
    return phrase


def verbPhrase():
    """Builds and returns a verb phrase."""
    phrase = random.choice(verbs) + " " + nounPhrase()
    if random.choice(prepRange) == 1:
        phrase += " " + prepositionalPhrase()
    return phrase


def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()


def main():
    """Allows the user to input the number of sentences
    to generate."""

    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())


# The entry point for program execution
if __name__ == "__main__":
    main()
