# Write a Python program to change a given string to a new string where the first and last chars have been exchanged
# Sample: ‘abcdefgh’

x='abcdefgh'
print(x[len(x)-1]+x[1:len(x)-1]+x[0])