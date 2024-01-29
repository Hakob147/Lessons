# Write a Python function to check whether a number is in a given range.

def check_the_number(number, start_range, end_range):
    result = False
    if start_range <= number <= end_range or end_range <= number <= start_range:
        result = True
    return result
x = check_the_number(10,12,40)
print(x)
