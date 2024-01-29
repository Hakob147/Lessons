# Vowel Counter

# Write a program that takes a string as input and counts the number of vowels (a, e, i, o, u) in the string. Use a for
# loop, an if statement, and the in operator to check if a character is a vowel.

text = input("Enter the text ")
vowels = ["a", "e", "i", "o", "u"]
count = 0
for n in text:
    if n in vowels:
        count = count+1
print(count)