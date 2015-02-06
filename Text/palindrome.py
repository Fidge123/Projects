# **Check if Palindrome** - Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”

user_string = input("Enter a possible palindrome: ")

if user_string == user_string[::-1]:
    print("This is a palindrome.")
else:
    print("This isnt a palindrome.")
