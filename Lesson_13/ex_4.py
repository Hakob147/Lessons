# Write a Python program to find intersection of two given arrays using
# Lambda.

list_1 = [1, 2, 3, 5, 7, 8, 9, 10]
list_2 = [1, 2, 4, 8, 9]
list_3 = list(filter(lambda x: x in list_2,list_1))
print(list_3)