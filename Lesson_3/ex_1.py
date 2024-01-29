# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.

# Sample String : 'w3'


#Option 1
x = "w3"
print(2*x)

#Option 2
x = "w3"
print(x+x)

#Option 3
x = "w3"
print(x[::]+x[::])

#Option 4
x = "w3"
print(x[:2]+x[0:])