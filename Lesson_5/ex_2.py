# Write a Python program to get the largest number from a list

list_1 = [1, 4, 9, 20, 8]
largest_number = list_1[0]
for number in list_1:
    if number > largest_number:
        largest_number = number
    else:
        pass
print(largest_number)

