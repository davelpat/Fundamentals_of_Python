"""
Instructions for programming Exercise 5.9

In Case Study: Nondirective Psychotherapy, when the patient addresses the
therapist personally, the therapist’s reply does not change persons
appropriately. To see an example of this problem, test the program with “you are
not a helpful therapist.” Fix this problem by repairing the dictionary of
replacements.

An example of the program input and output is shown below:

Good morning, I hope you are well today.
What can I do for you?

>> You can help me
Many of my patients tell me the same thing.

>> your abilites are limited
Why do you say that my abilites are limited

>> Quit
Have a nice day!
"""

"""
Instructions for programming Exercise 5.10

Conversations often shift focus to earlier topics. Modify the therapist program
to support this capability. Add each patient input to a history list. Then,
occasionally choose an element at random from this list, change persons, and
prepend (add at the beginning) the qualifier “Earlier you said that” to this
reply. Make sure that this option is triggered only after several exchanges have
occurred.

An example of the program input and output is shown below:

Good morning, I hope you are well today.
What can I do for you?

>> everyone hates me
Please tell me more.

>> my professor thinks I cheated
Why do you say that your professor thinks you cheated

>> he thought he saw me with my phone out during an exam
Many of my patients tell me the same thing.

>> but it was just my calculator
Please tell me more.

>> his class is my favorite!
Please tell me more.

>> even though it is at eight, I love getting up for it
Earlier you said that your professor thinks you cheated

>> I never would
Can you explain why you never would

>> quit
Have a nice day! 
"""

"""
File: doctor.py
Project 5.9
Conducts an interactive session of nondirective psychotherapy.
Fixes problem of responding to sentences that address the doctor
using second-person pronouns.
"""

import random

hedges = ("Please tell me more.",
          "Many of my patients tell me the same thing.",
          "Please continue.")

qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ")

# The fix is in this dictionary, third line of data
replacements = {"I":"you", "me":"you", "my":"your",
                "we":"you", "us":"you", "mine":"yours",
                "you":"I", "your":"my", "yours":"mine"}

change_topic = "Earlier you said that "

history = []

def reply(sentence):
    """Implements two different reply strategies."""
    probability = random.randint(1, 4)
    hist_size = len(history)
    if probability == 1:
        return random.choice(hedges)
    elif hist_size > 4 and probability == 2:
        return change_topic + changePerson(history[random.randint(1, hist_size - 2)])
    else:
        return random.choice(qualifiers) + changePerson(sentence)

def changePerson(sentence):
    """Replaces first person pronouns with second person
    pronouns."""
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords)

def main():
    """Handles the interaction between patient and doctor."""
    print("Good morning, I hope you are well today.")
    print("What can I do for you?")
    while True:
        sentence = input("\n>> ")
        history.append(sentence)
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        print(reply(sentence))

# The entry point for program execution
if __name__ == "__main__":
    main()