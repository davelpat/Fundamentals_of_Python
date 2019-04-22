"""
An employee’s total weekly pay equals the hourly wage
multiplied by the total number of regular hours, plus any overtime pay.

Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage.

Write a program that takes as inputs the hourly wage, total regular hours, and total overtime hours
and displays an employee’s total weekly pay.

Below is an example of the program inputs and output:

Enter the wage: $15.50
Enter the regular hours: 40
Enter the overtime hours: 12

The total weekly pay is $899.0
"""

# Get employee weekly data
wage = float(input("Enter the wage: "))
regHours = float(input("Enter the regular hours: "))
overtime = float(input("Enter the overtime hours: "))

# Calculate the pay
pay = wage * regHours + wage * overtime * 1.5

# and display it
print("The total weekly pay is $"+str(pay))
