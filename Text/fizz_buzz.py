# **Fizz Buzz** - Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

fizz = 0
buzz = 0
fizzbuzz = 0

for x in range(1, 101):
    if x % 3 == 0:
        if x % 5 == 0:
            print("FizzBuzz")
            fizzbuzz += 1
        else:
            print("Fizz")
            fizz += 1
    elif x % 5 == 0:
        print("Buzz")
        buzz += 1
    else:
        print(x)

print()
print("Fizz: ", fizz)
print("Buzz: ", buzz)
print("FizzBuzz: ", fizzbuzz)
print("Numbers: ", str(100 - fizz - buzz - fizzbuzz))
