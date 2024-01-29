#  Math Operations Exercise:
# Write a function that calculates the square root of a number using the math module.

import math

def calculate_square(number):
    if number <0:
        raise Exception("Cannot calculate square of negative number")
    return math.sqrt(number)

x = calculate_square(100)
print(x)