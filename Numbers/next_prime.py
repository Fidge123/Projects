# **Next Prime Number** - Have the program find prime numbers until the user chooses to stop asking for the next one.

calc_next = "y"
primes = []
current_number = 2
is_prime = True
found_prime = False

while calc_next == "y":
    calc_next = input("Calculate next prime (y/n)? ")

    while calc_next != "y" and calc_next != "n":
        calc_next = input("Invalid input! Calculate next prime (y/n)? ")

    while found_prime == False:
        for p in primes:
            if current_number % p == 0:
                is_prime = False

        if is_prime == True:
            primes.append(current_number)
            found_prime = True
        else:
            current_number += 1
            is_prime = True

    print("Next prime is ", current_number)

    found_prime = False
    current_number += 1
