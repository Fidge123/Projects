# **Find Cost of Tile to Cover W x H Floor** - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.

from math import ceil

f_width = float(input("Enter the width of the floor in m: "))
f_height = float(input("Enter the height of the floor in m: "))
f_area = f_width * f_height
print("The floor is ", f_width, "m by ", f_height, "m for a total of ", f_area, "m2.")
print()

t_width = float(input("Enter the width of a single tile in cm: "))
t_height = float(input("Enter the height of a single tile in cm: "))
t_cost = float(input("Enter the cost per tile in Euro: "))

total_amount = ceil(f_width * 100 / t_width) * ceil(f_height * 100 / t_height)
total_cost = total_amount * t_cost
print("You have to buy ", total_amount, " tiles for a total of ", total_cost, " Euro.")
