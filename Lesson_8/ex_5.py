# You are given three lists, list1, list2, and list3. Your task is to implement a programm that takes these lists and prints the following:

# The set of elements that are common to all three lists.
list_1 = ["a", "b", "c", "d"]
list_2 = ["c", "d", "e", "f"]
list_3 = ["d", "e", "f", "g"]
list_common = set(list_1) & set(list_2) & set(list_3)
print(list_common)

# The set of elements that are present in at least two of the three lists, but not in all three
list_two_1 = set(list_1) & set(list_2) - set(list_3)
list_two_2 = set(list_1) & set(list_3) - set(list_2)
list_two_3 = set(list_2) & set(list_3) - set(list_1)
print(list_two_1, list_two_2, list_two_3)

# The set of elements that are unique to each list (present in only one list).
list_unique_1 = set(list_1) - set(list_2) - set(list_3)
list_unique_2 = set(list_2) - set(list_1) - set(list_3)
list_unique_3 = set(list_3) - set(list_2) - set(list_1)
print(list_unique_1, list_unique_2, list_unique_3)