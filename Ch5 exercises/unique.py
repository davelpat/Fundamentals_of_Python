"""
Instructions for programming Exercise 5.7

Write a program that inputs a text file. The program should print the unique
words in the file in alphabetical order.

An example file along with the correct output is shown below:

example.txt

the quick brown fox jumps over the lazy dog

Enter the input file name: example.txt

brown
dog
fox
jumps
lazy
over
quick
the
"""

file_name = input("Enter the input file name: ")
fIn = open(file_name, 'r')

dyct = {}
for line in fIn:
    words = line.split()
    for word in words:
        if not word in dyct:
            dyct[word] = 1

for word in sorted(dyct.keys()):
    print(word)
