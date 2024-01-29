# Write a Python program that input a sentence and return the longest word and the length
# of the longest one.


sentence = input("Enter the sentence ")
list_1 = sentence.split()
longest = list_1[0]
for n in list_1:
    if len(n) > len(longest):
        longest = n
a = longest
b = len(longest)

print(f"The longest word is {a} and it's length is {b}")