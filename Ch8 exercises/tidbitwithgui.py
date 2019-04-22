"""
Instructions for programming Exercise 8.7

The TidBit Computer Store (Chapter 3, Project 10) has a credit plan for computer
purchases. Inputs are the annual interest rate and the purchase price. Monthly
payments are 5% of the listed purchase price, minus the down payment, which must
be 10% of the purchase price.

Write a GUI-based program that displays labeled fields for the inputs and a text
area for the output. The program should display a table, with appropriate
headers, of a payment schedule for the lifetime of the loan. Each row of the
table should contain the following items:

The month number (beginning with 1)
The current total balance owed
The interest owed for that month
The amount of principal owed for that month
The payment for that month
The balance remaining after payment

The amount of interest for a month is equal to balance * rate / 12. The amount
of principal for a month is equal to the monthly payment minus the interest
owed. Your program should include separate classes for the model and the view.
The model should include a method that expects the two inputs as arguments and
returns a formatted string for output by the GUI.
"""

"""
Program: tidbit.py
Project 3.10

Print a payment schedule for a loan to purchase a computer.

Input
   purchase price

Constants
   annual interest rate = 12%
   downpayment = 10% of purchase price
   monthly payment = 5% of purchase price

"""

from breezypythongui import EasyFrame


# other imports


class TidbitGUI(EasyFrame):

    def __init__(self):
        """Sets up the window, labels, and buttons"""
        EasyFrame.__init__(self)

        # Label and field for the purchase price
        self.addLabel(text="Purchase price",
                      row=0, column=0)
        self.priceField = self.addFloatField(value=0.0,
                                             row=0, column=1,
                                             precision=2)

        # Label and field for the interest rate
        self.addLabel(text="Annual interest",
                      row=1, column=0)
        self.rateField = self.addIntegerField(value=0,
                                              row=1, column=1)

        # The calculate button
        self.button = self.addButton(text="Calculate",
                                     row=2, column=0,
                                     columnspan=2,
                                     command=self.calculate_payments)
        self.button.bind("<Return>", lambda event: self.calculate_payments())

        self.outputArea = self.addTextArea("", row=3, column=0, columnspan=3,
                                           width=84, height=15)

    def calculate_payments(self):
        ANNUAL_RATE = self.rateField.getNumber() / 100
        MONTHLY_RATE = ANNUAL_RATE / 12

        purchasePrice = self.priceField.getNumber()

        monthlyPayment = .05 * (purchasePrice - (.10 * purchasePrice))
        month = 1
        balance = purchasePrice
        self.outputArea.setText(
            "Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance\n")
        while balance > 0:
            if monthlyPayment > balance:
                monthlyPayment = balance
                interest = 0
            else:
                interest = balance * MONTHLY_RATE
                principal = monthlyPayment - interest
                remaining = balance - monthlyPayment
                monthly_numbers = str("%2d%15.2f%15.2f%17.2f%17.2f%17.2f\n" % \
                                      (month, balance, interest, principal, monthlyPayment, remaining))
                self.outputArea.appendText(monthly_numbers)
                balance = remaining
                month += 1


def main():
    """Instantiates and pops up the window"""
    TidbitGUI().mainloop()


if __name__ == '__main__':
    main()
