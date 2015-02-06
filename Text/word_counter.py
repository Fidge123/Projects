# **Count Words in a String** - Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.

user_string = input("Enter filename: ")
words = 0
previous = " "

with open(user_string, 'r') as f:
    data = f.read().split()
    print("There are ", len(data), " words.")
