"""
Instructions for programming Exercise 5.8

A file concordance tracks the unique words in a file and their frequencies.
Write a program that displays a concordance for a file. The program should
output the unique words and their frequencies in alphabetical order. Variations
are to track sequences of two words and their frequencies, or n words and their
frequencies.

Below is an example file along with the program input and output:

example.txt

I AM SAM I AM SAM SAM I AM

Enter the input file name: example.txt

AM 3
I 3
SAM 3
"""

file_name = input("Enter the input file name: ")
fIn = open(file_name, 'r')

dyct = {}
for line in fIn:
    words = line.split()
    for word in words:
        if not word in dyct:
            dyct[word] = 1
        else:
            dyct[word] += 1


for word in sorted(dyct.keys()):
    print(word, dyct[word])
