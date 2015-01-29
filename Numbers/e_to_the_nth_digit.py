# **Find e to the Nth Digit** - Just like the previous problem, but with e instead of PI. Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.

import math
import decimal

getcontext().prec = 50

n = input("Calculate 'e' to this decimal place: ")
if int(n) < 50:
	result = Decimal(math.trunc(math.e * pow(10, int(n)))/pow(10, int(n)))
	print(result)
else:
	print(Decimal(math.e))
	print("The maximum precision is 50.")
