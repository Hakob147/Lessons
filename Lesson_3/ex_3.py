# Write a Python program to remove the n-th index character from a nonempty string

#Sample string: ‘abcdefgh’
# n - 3

x="abcdefgh"
n=3
print(x[:n]+x[n+1:])
