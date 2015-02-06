# **Count Vowels** - Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.

user_string = input("Enter a sentence: ").lower()

vowels = ["a", "e", "i", "o", "u"]
vowel_counter = [0, 0, 0, 0, 0]

for x in user_string:
    for y in range(0, 5):
        if x == vowels[y]:
            vowel_counter[y] += 1


print("A: ", vowel_counter[0])
print("E: ", vowel_counter[1])
print("I: ", vowel_counter[2])
print("O: ", vowel_counter[3])
print("U: ", vowel_counter[4])
print("Total: ", sum(vowel_counter))
