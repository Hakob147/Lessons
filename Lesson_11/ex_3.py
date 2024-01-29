# Write a Python function to return the even numbers from a given list.

def return_even_numbers(numbers):
    list_1 = []
    for i in numbers:
        if i % 2 ==0:
            list_1.append(i)
    return list_1
x = return_even_numbers([1, 2, 3, 4, 5, 6, 7, 8])
print(x)
