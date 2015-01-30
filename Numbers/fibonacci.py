# **Fibonacci Sequence** - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

n = int(input("Calculate nth Fibonacci number: "))

fib = 1
f1 = 1
f2 = 0

for x in range(0, n):
    fib = f1 + f2
    f2 = f1
    f1 = fib
    print(fib)
