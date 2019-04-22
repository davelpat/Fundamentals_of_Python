"""
Instructions for programming Exercise 4.10

Write a script named dif.py. This script should prompt the user for the names of
two text files and compare the contents of the two files to see if they are the
same.

If they are, the script should simply output "Yes". If they are not, the script
should output "No", followed by the first lines of each file that differ from
each other. The input loop should read and compare lines from each file. The
loop should break as soon as a pair of different lines is found.

Below are examples of the program input and output along with relevant files:

one.txt:

This is text.
abc
123
sameAsOne.txt:

This is text.
abc
123
differentFromOne.txt

This is text.
xyz
123
Comparing files that are the same:

Enter the first file name: one.txt
Enter the second file name: sameAsOne.txt

Yes
Comparing files that are different:

Enter the first file name: one.txt
Enter the second file name: differentFromOne.txt

No
abc
xyz
"""

firstFile = input("Enter the first file name: ")
secondFile = input("Enter the second file name: ")

f1 = open(firstFile, "r")
f2 = open(secondFile, "r")

while True:
    line1 = f1.readline()
    line2 = f2.readline()

    if line1 == "" or line2 == "":
        if line1 == "" and line2 == "":
            print("Yes")
        elif line1 == "":
            print("No")
            print("")
            print(line2)
        else:
            print("No")
            print(line1)
            print("")
        break
    elif line1 != line2:
        print("No")
        print(line1)
        print(line2)
        break

f1.close
f2.close
