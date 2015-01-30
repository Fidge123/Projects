# **Find e to the Nth Digit** - Just like the previous problem, but with e instead of PI. Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.

from decimal import Decimal, getcontext, ROUND_DOWN
from math import factorial

precision = int(input("Calculate e to the nth digit: "))
getcontext().prec = precision + 5
getcontext().rounding = ROUND_DOWN

e = Decimal(0)

for x in range(0, precision + 1):
    e += Decimal(2 * x + 1) / Decimal(factorial(2 * x))

getcontext().prec = precision

print(+e)
