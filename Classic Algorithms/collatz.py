# **Collatz Conjecture** - Start with a number *n > 1*. Find the number of steps it takes to reach one using the following process: If *n* is even, divide it by 2. If *n* is odd, multiply it by 3 and add 1.

n = int(input("Find number of steps to complete the Collatz conjecture: "))
steps = 0

if n < 1:
    n = int(input("Number not valid. Enter number greater than 1: "))

while n != 1:
    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = 3 * n + 1
    steps += 1
print(steps)
