"""
In a factory, a printer prints labels for boxes.
For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.
The colors used by the printer are recorded in a control string.

For example, a "good" control string would be "aaabbbbhaijjjm", meaning the printer used color a four times, color b four times, color h one time, etc.

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.
You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string.
Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from ato z.

Examples:
    s="aaabbbbhaijjjm"
    printer_error(s) => "0/14"

    s="aaaxbbbbyyhwawiwjjjwwm"
    printer_error(s) => "8/22"
"""

import string

def printer_error(txt):
    
    error_count = 0
    
    for char in txt:
        if char in string.ascii_lowercase[13:]:  # n --> z == error codes
            error_count += 1
            
    return f"{error_count}/{len(txt)}"
