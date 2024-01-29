# Write a function that finds the index of a given element in a list. If the element is not
# present, return -1.

def find_index(list_1,number):
    index = -1
    for n in range(len(list_1)):
        if list_1[n] == number:
            index = n
    return index
a = find_index([10,20,30],30)
print(a)
