"""
Instructions for programming Exercise 9.5

The Doctor program described in Chapter 5 combines the data model of a doctor
and the operations for handling user interaction. Restructure this program
according to the model/view pattern so that these areas of responsibility are
assigned to separate sets of classes.

The program should include a Doctor class with an interface that allows one to
obtain a greeting, a signoff message, and a reply to a patient’s string.

To implement the greeting, define a method named greeting for the Doctor class.
To implement the signoff message, define a method named farewell for the Doctor
class. Both greeting and farewell should return a string with a greeting or
farewell message respectively. The reply function is defined for you, it should
be added as a method for the Doctor class.

The rest of the program, in a separate main program module, handles the user’s
interactions with the Doctor object. Develop this program with a terminal-based
user interface.
"""

"""
File: doctor.py
Starter 9.5
Conducts an interactive session of nondirective psychotherapy.
Adds a history list of earlier patient sentences, which can
be chosen for replies to shift the conversation to an earlier topic.
"""

from breezypythongui import EasyFrame
import random


class Response(EasyFrame):
    HEDGES = ("Please tell me more.",
              "Many of my patients tell me the same thing.",
              "Please coninue.")

    QUALIFIERS = ("Why do you say that ",
                  "You seem to think that ",
                  "Can you explain why ")

    REPLACEMENTS = {"I": "you", "me": "you", "my": "your",
                    "we": "you", "us": "you", "mine": "yours",
                    "you": "I", "your": "my", "yours": "mine"}

    history = []

    def __init__(self):
        pass

    def get_hedge(self):
        response = random.choice(self.HEDGES)
        return response

    def change_topic(self):
        return "Earlier you said that " + \
               self.changePerson(random.choice(self.history))

    def continue_topic(self, sentence):
        response = random.choice(self.QUALIFIERS) + self.changePerson(sentence)
        self.history.append(response)
        return response

    def changePerson(self, sentence):
        """Replaces first person pronouns with second person
        pronouns."""
        words = sentence.split()
        replyWords = []
        for word in words:
            replyWords.append(self.REPLACEMENTS.get(word, word))
        return " ".join(replyWords)


class Doctor(EasyFrame):
    def reply(sentence):
        """Implements three different reply strategies."""
        probability = random.randint(1, 5)
        if probability in (1, 2):
            # Just hedge
            answer = Response().get_hedge()
        elif probability == 3 and len(Response().history) > 3:
            # Go back to an earlier topic
            answer = Response().change_topic()
        else:
            # Transform the current input
            answer = Response().continue_topic(sentence)
        # Always add the current sentence to the history list
        return answer

    def greeting():
        return "Good morning, I hope you are well today.\nWhat can I do for you?"

    def farewell():
        return "Have a nice day!"


def main():
    """Handles the interaction between patient and doctor."""
    print(Doctor.greeting())
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print(Doctor.farewell())
            break
        print(Doctor.reply(sentence))


# The entry point for program execution
if __name__ == "__main__":
    main()
