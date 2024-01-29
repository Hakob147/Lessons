# Write a Python program to get the smallest number from a list

list_1 = [1, 4, 9, 20, 8, -5]
smallest_number = list_1[0]
for number in list_1:
    if number < smallest_number:
        smallest_number = number
    else:
        pass
print(smallest_number)

