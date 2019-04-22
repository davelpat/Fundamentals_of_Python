"""
Instructions

Teachers in most school districts are paid on a schedule that provides a salary
based on their number of years of teaching experience.

For example, a beginning teacher in the Lexington School District might be paid
$30,000 the first year. For each year of experience after this first year, up to
10 years, the teacher receives a 2% increase over the preceding value.

Write a program that displays a salary schedule, in tabular format, for teachers
in a school district. The inputs are:

Starting salary
Annual percentage increase
Number of years for which to print the schedule
Each row in the schedule should contain the year number and the salary for that year

An example of the program input and output is shown below:

Enter the starting salary: $30000
Enter the annual % increase: 2
Enter the number of years: 10

Year   Salary
-------------
 1    30000.00
 2    30600.00
 3    31212.00
 4    31836.24
 5    32472.96
 6    33122.42
 7    33784.87
 8    34460.57
 9    35149.78
10    35852.78
"""

salary = int(input("Please enter starting salary in dollars: "))
incr = float(input("Please enter the percent annual increase: ")) / 100
service = int(input("Please enter the years of service (max = 10): "))

print("%4s%10s" % ("Year", "Salary"))
print("-"*14)
for year in range(1, service + 1):
    print("%-6i%0.2f" % (year, salary))
    salary += salary * incr
