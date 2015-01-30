# **Prime Factorization** - Have the user enter a number and find all Prime Factors (if there are any) and display them.

from fractions import gcd

n = int(input("Calculate all prime factors: "))

while n != 1:
    x_fixed = 2
    cycle_size = 2
    x = 2
    h = 1

    while h == 1:
        count = 1
        while (count <= cycle_size and h == 1):
            x = (x * x + 1) % n
            count = count + 1
            h = gcd(x - x_fixed, n)

        if h != 1:
            break

        cycle_size *= 2
        x_fixed = x

    n = int(n / h)
    print(h)
