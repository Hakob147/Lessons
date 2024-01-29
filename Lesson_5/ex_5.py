# Write a Python program to remove duplicates from a list

#Option 1

l = [1, 1, 23, 65, 5, 5]
unique_set = set(l)
unique_list = list(unique_set)

print(unique_list)

#Option 2

l_2 = [1, 1, 23, 65, 5, 5]
unique_l_2 = []
for n in l_2:
    if n not in unique_l_2:
        unique_l_2.append(n)
print(unique_l_2)