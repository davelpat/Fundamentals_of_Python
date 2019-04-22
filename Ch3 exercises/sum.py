"""
Instructions

Write a program that receives a series of numbers from the user and allows the
user to press the enter key to indicate that he or she is finished providing
inputs. After the user presses the enter key, the program should print:

The sum of the numbers
The average of the numbers
An example of the program input and output is shown below:

Enter a number or press Enter to quit: 1
Enter a number or press Enter to quit: 2
Enter a number or press Enter to quit: 3
Enter a number or press Enter to quit:

The sum is 6.0
The average is 2.0
"""

cnt = 0
tot = 0.0

while True:
    num = input("Enter a number or press Enter to quit: ")
    if num == "":
        break
    tot += float(num)
    cnt += 1

if cnt > 0:
    print("The sum is", tot)
    print("The average is", tot / cnt)
else:
    print("you didn't enter any numbers")
