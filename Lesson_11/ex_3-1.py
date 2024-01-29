# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.

def factorial(number):
    sum = 1
    for i in range(1,number+1):
        sum = sum * i
    return print(sum)
factorial(5)