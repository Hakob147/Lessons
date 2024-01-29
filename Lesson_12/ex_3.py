# Write a function that calculates the average of a list of numbers.

def average(number):
    sum_numbers = 0
    for n in number:
        sum_numbers += n
    result = sum_numbers / len(number)
    return result
a = average([2,10,21])
print(a)
