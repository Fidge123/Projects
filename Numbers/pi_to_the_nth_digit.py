# **Find PI to the Nth Digit** - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.

import math
import decimal

getcontext().prec = 50

n = input("Calculate Pi to this decimal place: ")
if int(n) < 50:
	result = Decimal(math.trunc(math.pi * pow(10, int(n)))/pow(10, int(n)))
	print(result)
else:
	print(Decimal(math.pi))
	print("The maximum precision is 50.")
