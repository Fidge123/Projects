# **Find PI to the Nth Digit** - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.

from decimal import Decimal, getcontext, ROUND_DOWN

precision = int(input("Calculate pi to the nth digit: "))
getcontext().prec = precision + 5
getcontext().rounding = ROUND_DOWN

pi = Decimal(0)
base16 = Decimal(1)

for x in range(0, precision + 1):
    a = Decimal(4) / Decimal(8 * x + 1)
    b = Decimal(-2) / Decimal(8 * x + 4)
    c = Decimal(-1) / Decimal(8 * x + 5)
    d = Decimal(-1) / Decimal(8 * x + 6)
    pi += Decimal(a + b + c + d) / Decimal(base16)
    base16 *= Decimal(16)

getcontext().prec = precision

print(+pi)
