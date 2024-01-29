# Write a Python program to add two given lists using map and lambda

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

list_3 = list(map(lambda a,b: a +b,list_1,list_2 ))
print(list_3)