# **Sorting** - Implement two types of sorting algorithms: ~~Merge sort~~ and bubble sort.

import random

size = int(input("How many number should be sorted? "))

items = []

for x in range(0, size):
    items.append(x)
random.shuffle(items)

print("Starting to sort!")
num_swapped = 0
num_accessed = 0
is_sorted = False

while is_sorted == False:
    is_sorted = True
    for x in range(0, size - 1):
        num_accessed += 1
        if items[x] < items[x + 1]:
            temp = items[x]
            items[x] = items[x + 1]
            items[x + 1] = temp
            num_swapped += 1
            is_sorted = False

print("Accessed:", num_accessed, "Swapped:", num_swapped)
print("Successfully sorted.")
