# **Pig Latin** - Pig Latin is a game of alterations played on the English language game. To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.

user_string = input("Enter a word to translate to pig latin: ")
vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

for x in range(0, len(user_string)):
    if user_string[0] in vowels:
        pig_string = user_string + "-way"
        print(pig_string)
        break
    if user_string[x] in vowels:
        pig_string = user_string[x::1] + "-" + user_string[0:x:] + "ay"
        print(pig_string)
        break
