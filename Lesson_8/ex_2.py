# Write a Python function that takes two sets as input and returns a new set containing all
# unique elements from both input sets.

set_1 = {"a", "b", "c", "d"}
set_2 = {"c", "d", "e", "f"}
set_3 = set_1 | set_2
print(set_3)