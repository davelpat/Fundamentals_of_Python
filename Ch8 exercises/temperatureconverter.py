"""
Instructions for programming Exercise 8.3

Write a GUI-based program that allows the user to convert temperature values between degrees Fahrenheit
and degrees Celsius. The interface should have labeled entry fields for these two values.

These components should be arranged in a grid where the labels occupy the first row and the
corresponding fields occupy the second row.

At start-up, the Fahrenheit field should contain 32.0, and the Celsius field should contain 0.0.

The third row in the window contains two command buttons, labeled >>>> and <<<<.
When the user presses the first button, the program should use the data in the Celsius field to compute the
Fahrenheit value, which should then be output to the Fahrenheit field.
The second button should perform the inverse function.
"""

"""
Instructions for programming Exercise 8.4

Modify the temperature conversion program so that it responds to the user’s
press of the return or enter key. If the user presses this key when the
insertion point is in a given field, the action which uses that field for input
is triggered. 
"""

"""
File: temperatureconverter.py
Project 8.3
Temperature conversion between Fahrenheit and Celsius.
Illustrates the use of numeric data fields.
"""

from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):
    """A termperature conversion program."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Temperature Converter")

        # Label and field for Celsius
        self.addLabel(text = "Celsius",
                      row = 0, column = 0)
        self.celsiusField = self.addFloatField(value = 0.0,
                                               row = 1,
                                               column = 0,
                                               precision = 2)
        self.celsiusField.bind("<Return>", lambda event: self.computeFahr())

        # Label and field for Fahrenheit
        self.addLabel(text = "Fahrenheit",
                      row = 0, column = 1)
        self.fahrField = self.addFloatField(value = 32.0,
                                            row = 1,
                                            column = 1,
                                            precision = 2)
        self.fahrField.bind("<Return>", lambda event: self.computeCelsius())


        # Celsius to Fahrenheit button
        self.addButton(text = ">>>>",
                       row = 2, column = 0,
                       command = self.computeFahr)

        # Fahrenheit to Celsius button
        self.addButton(text = "<<<<",
                       row = 2, column = 1,
                       command = self.computeCelsius)

    # The controller methods
    def computeFahr(self):
        """Inputs the Celsius degrees
        and outputs the Fahrenheit degrees."""
        degrees = self.celsiusField.getNumber()
        degrees = degrees * 9 / 5 + 32
        self.fahrField.setNumber(degrees)

    def computeCelsius(self):
        """Inputs the Fahrenheit degrees
        and outputs the Celsius degrees."""
        degrees = self.fahrField.getNumber()
        degrees = (degrees - 32) * 5 / 9
        self.celsiusField.setNumber(degrees)

def main():
    """Instantiate and pop up the window."""
    TemperatureConverter().mainloop()

if __name__ == "__main__":
    main()
