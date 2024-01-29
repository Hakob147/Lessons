# Write a function that calculates the sum of squares of numbers from 1 to n

def sum_of_squares(num):
    result = 0
    for n in range(num+1):
        result = result + n**2
    return result
x = sum_of_squares(4)
print(x)