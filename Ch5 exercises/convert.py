"""
Instructions for programming Exercise 5.5

In Chapter 4, we developed an algorithm for converting from binary to decimal.
You can generalize this algorithm to work for a representation in any base.
Instead of using a power of 2, this time you use a power of the base. Also, you
use digits greater than 9, such as A . . . F, when they occur.

In convert.py, define a function named repToDecimal that expects two arguments,
a string, and an integer. The second argument should be the base. For example,
repToDecimal("10", 8) returns 8, whereas repToDecimal("10", 16) returns 16.

The function should use a lookup table to find the value of any digit. Make sure
that this table (it is actually a dictionary) is initialized before the function
is defined. For its keys, use the 10 decimal digits (all strings) and the
letters A . . . F (all uppercase). The value stored with each key should be the
integer that the digit represents. (The letter A associates with the integer
value 10, and so on.) The main loop of the function should convert each digit to
uppercase, look up its value in the table, and use this value in the
computation. Include a main function that tests the conversion function with
numbers in several bases.

An example of main and correct output is shown below:

def main():
    print(repToDecimal('10', 10))
    print(repToDecimal('10', 8))
    print(repToDecimal('10', 2))
    print(repToDecimal('10', 16))
10
8
2
16
"""

"""
Instructions for programming Exercise 5.6

In convert.py, define a function decimalToRep that returns the representation of
an integer in a given base.

The two arguments should be the integer and the base.
The function should return a string.
It should use a lookup table that associates integers with digits.
Include a main function that tests the conversion function with numbers in
several bases.
An example of main and correct output is shown below:

def main():
    """Tests the function."""
    print(decimalToRep(10, 10))
    print(decimalToRep(10, 8))
    print(decimalToRep(10, 2))
    print(decimalToRep(10, 16)) 
10
12
1010
A 
"""

def gen_hex_lookup_tab(hexKeys):
    """ Define the hexidecimal lookup table, repTab"""
    repTab = {}
    i = 0
    for k in hexKeys:
        repTab[k] = i
        i += 1
    return repTab


hexKeys = list("0123456789ABCDEF")
repTab = gen_hex_lookup_tab(hexKeys)


def repToDecimal(rep_string, base):
    """ Takes a string representation of a number in some base and the base
        Returns the decimal equivalent"""
    decimal = int(0)
    exponent = len(rep_string) - 1
    for digit in rep_string:
        decimal += repTab[digit.upper()] * base ** exponent
        exponent -= 1
    return decimal

def decimalToRep(dec_value, base):
    """ Takes a decimal value to convert and the base to convert it to
        Returns a string representation of the converted value"""
    if dec_value == 0:
        return 0
    else:
        # print("Quotient Remainder Binary")
        rep_string = ""
        while dec_value > 0:
            remainder = dec_value % base  # look up the key
            dec_value = dec_value // base
            rep_string = hexKeys[remainder] + rep_string
            # print("%5d%8d%12s" % (dec_value, remainder, rep_string))
        return rep_string


def main():
    """Test the conversion function"""
    print(repToDecimal('10', 10))
    print(repToDecimal('10', 8))
    print(repToDecimal('10', 2))
    print(repToDecimal('10', 16))

    print(decimalToRep(10, 10))
    print(decimalToRep(10, 8))
    print(decimalToRep(10, 2))
    print(decimalToRep(10, 16))


if __name__ == '__main__':
    main()
