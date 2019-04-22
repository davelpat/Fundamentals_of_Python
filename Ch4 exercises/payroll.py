"""
Instructions for programming Exercise 4.12

The Payroll Department keeps a list of employee information for each pay period
in a text file. The format of each line of the file is the following: <last
name> <hourly wage> <hours worked>

Write a program that inputs a filename from the user and prints to the terminal
a report of the wages paid to the employees for the given period.

The report should be in tabular format with the appropriate header.
Each line should contain:
An employee’s name
The hours worked
The wages paid for that period.
An example of the program input and output is shown below:

Enter the file name: data.txt

Name            Hours      Total Pay
Lambert            34         357.00
Osborne            22         137.50
Giacometti          5         503.50
"""

LABELS = ("Name", "Hours", "Total Pay")
LABELS_FMT = "%-16s%6s%15s"
DATA_FMT = "%-16s%6.2f%15.2f"

# data field positions
NAME = 0
RATE = 1
HOURS = 2


data = input("Enter the file name: ")
timesheets = open(data, "r")


print(LABELS_FMT % LABELS)

for employee in timesheets:
    empData = employee.split()
    pay = float(empData[RATE]) * float(empData[HOURS])
    print(DATA_FMT % (empData[NAME], float(empData[HOURS]), pay))