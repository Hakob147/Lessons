# Write a Python function to sum all the numbers in a list.Sample List
def sum_list_numbers(number):
    result = 0
    for i in number:
        result = result + i
    return result
x = sum_list_numbers([1, 2, 3, 4, 5])
print(x)