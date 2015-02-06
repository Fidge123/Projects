# **Change Return Program** - The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

from math import floor, ceil

cost = float(input("Enter cost: "))
money_given = float(input("Enter money given: "))

coins = [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

difference = money_given * 100 - cost * 100

if difference < 0:
    print("There are", -difference, "Euro missing.")
else:
    for coin in coins:
        amount_of_coin = floor(difference / coin)

        if amount_of_coin != 0:
            if coin >= 100:
                print(amount_of_coin, "times", int(coin / 100), "Euro")
            else:
                print(amount_of_coin, "times", coin, "Cents")

            difference -= amount_of_coin * coin
