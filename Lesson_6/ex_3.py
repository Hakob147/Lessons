# Word Finder

# Write a program that takes a list of words and a target word as input.
# The program should find and print all words in the list that contain the
# target word. Use a for loop, the in operator, and an if statement to
# check if the target word is present in each word in the list.

words = input("Enter the words ")
list_1 = ["apple", "table", "pineapple"]
list_2 = []
for n in list_1:
    if words in n:
        list_2.append(n)
print(list_2)
