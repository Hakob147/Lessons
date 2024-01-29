# Write a program to check if two strings are balanced. For example, strings s1 and
# s2 are balanced if all the characters in the s1 are present in s2. The character’s
# position doesn’t matter.

s1 = input("Enter the s1 ")
s2 = input("Enter the s2 ")

result = True
for n in s1:
    if n not in s2:
        result = False

print(result)