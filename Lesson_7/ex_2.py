# Write a Python script that takes a list of words and return the longest word and the
# length of the longest one.


list_1 = ["apple", "notebook", "book"]
longest = list_1[0]
for n in list_1:
    if len(n) > len(longest):
        longest = n
a = longest
b = len(longest)

print(f"The longest word is {a} and it's length is {b}")