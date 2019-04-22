"""
File: taxformwithgui.py
Project 8.1
A GUI-based tax calculator.

Computes and prints the total tax, given the income and number of dependents
(inputs), and a standard deduction of $10,000, an exemption amount of $3,000.

Add radio button options for filing status to the tax calculator program of
Project 1. The user selects one of these options to determine the tax rate.
The Single option’s rate is 20%. The Married option is 15%. The Divorced
option is 10%. The default option is Single.
"""

from breezypythongui import EasyFrame


class TaxCalculator(EasyFrame):
    """Application window for the tax calculator."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title="Tax Calculator")

        # Label and field for the income
        self.addLabel(text="Gross Income",
                      row=0, column=0)
        self.incomeField = self.addFloatField(value=0.0,
                                              row=0, column=1,
                                              precision=2)

        # Label and field for the number of dependents
        self.addLabel(text="Dependents",
                      row=1, column=0)
        self.depField = self.addIntegerField(value=0,
                                             row=1, column=1)

        # Radio buttons for filing status
        self.addLabel(text="Filing status:",
                      row=2, column=0)
        self.statusGroup = self.addRadiobuttonGroup(row=3, column=0,
                                                    rowspan=3)
        self.single = self.statusGroup.addRadiobutton(text="Single")
        self.married = self.statusGroup.addRadiobutton(text="Married")
        self.divorced = self.statusGroup.addRadiobutton(text="Divorced")
        # default status is Single
        self.statusGroup.setSelectedButton(self.single)

        # The command button
        self.addButton(text="Compute",
                       row=6, column=0,
                       columnspan=2,
                       command=self.computeTax)

        # Label and field for the tax
        self.addLabel(text="Total tax",
                      row=7, column=0)
        self.taxField = self.addFloatField(value=0.0,
                                           row=7, column=1,
                                           precision=2)

    # The event handler method for the button
    def computeTax(self):
        """Obtains the data from the input field and uses
        them to compute the tax, which is sent to the
        output field."""

        # Initialize the constants
        STANDARD_DEDUCTION = 10000.0
        DEPENDENT_DEDUCTION = 3000.0

        # Set tax rate based on marial status
        status = self.statusGroup.getSelectedButton()["text"]
        if status == "Married":
            TAX_RATE = 0.15
        elif status == "Divorced":
            TAX_RATE = 0.10
        else:
            TAX_RATE = 0.20

        # Compute the income tax
        taxableIncome = self.incomeField.getNumber() - STANDARD_DEDUCTION - \
                        DEPENDENT_DEDUCTION * self.depField.getNumber()
        self.taxField.setNumber(round(taxableIncome * TAX_RATE, 2))


def main():
    TaxCalculator().mainloop()


if __name__ == "__main__":
    main()
