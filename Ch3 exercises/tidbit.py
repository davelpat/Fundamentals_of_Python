"""
Instructions

The credit plan at TidBit Computer Store specifies a 10% down payment and an
annual interest rate of 12%. Monthly payments are 5% of the listed purchase
price, minus the down payment.

Write a program that takes the purchase price as input. The program should
display a table, with appropriate headers, of a payment schedule for the
lifetime of the loan. Each row of the table should contain the following items:

The month number (beginning with 1)
The current total balance owed
The interest owed for that month
The amount of principal owed for that month
The payment for that month
The balance remaining after payment
The amount of interest for a month is equal to balance × rate / 12.

The amount of principal for a month is equal to the monthly payment minus the
interest owed.

An example of the program input and output is shown below:

Enter the puchase price: 200

Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance
 1         200.00           2.00             8.00            10.00        190.00
 2         190.00           1.90             8.10            10.00        180.00
 3         180.00           1.80             8.20            10.00        170.00
 4         170.00           1.70             8.30            10.00        160.00
 5         160.00           1.60             8.40            10.00        150.00
 6         150.00           1.50             8.50            10.00        140.00
 7         140.00           1.40             8.60            10.00        130.00
 8         130.00           1.30             8.70            10.00        120.00
 9         120.00           1.20             8.80            10.00        110.00
10         110.00           1.10             8.90            10.00        100.00
11         100.00           1.00             9.00            10.00         90.00
12          90.00           0.90             9.10            10.00         80.00
13          80.00           0.80             9.20            10.00         70.00
14          70.00           0.70             9.30            10.00         60.00
15          60.00           0.60             9.40            10.00         50.00
16          50.00           0.50             9.50            10.00         40.00
17          40.00           0.40             9.60            10.00         30.00
18          30.00           0.30             9.70            10.00         20.00
19          20.00           0.20             9.80            10.00         10.00
20          10.00           0.10             9.90            10.00          0.00
"""

balance = price = float(input("Enter the puchase price: "))
downPayment = price * 0.1
apr = 0.12
monthlyPayment = (price - downPayment) * 0.05
month = 1

# Format for the column headers
hdrFmt = "%5s%18s%17s%18s%9s%16s"
print(hdrFmt % ("Month", "Starting Balance", "Interest to Pay", "Principal to Pay", "Payment", "Ending Balance"))

# Format for the table records
tblFmt = "%5i%18.2f%17.2f%18.2f%9.2f%16.2f"

while balance > 0:
    if balance <= monthlyPayment:
        monthlyInterest = 0
        monthlyPrincipal = balance
        newBalance = 0
        monthlyPayment = balance
    else:
        monthlyInterest = balance * apr / 12
        monthlyPrincipal = monthlyPayment - monthlyInterest
        newBalance = balance - monthlyPayment

    print(tblFmt % (month, balance, monthlyInterest, monthlyPrincipal, monthlyPayment, newBalance))
    month += 1
    balance = newBalance