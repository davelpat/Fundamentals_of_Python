"""
File: rgb.py
"""

def rgbToHexString(rgbTriple):
    """Converts the rgbTriple (R, G, B) to a hex string
    of the form #RRGGBB."""
    hexString = ""
    for i in rgbTriple:    # Iterate through the triple
        twoDigits = hex(i)[2:]
        if len(twoDigits) == 1:
            twoDigits = '0' + twoDigits
        hexString += twoDigits
    return '#' + hexString
