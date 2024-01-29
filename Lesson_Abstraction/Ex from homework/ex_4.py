# List Exercise:
# Write a function that takes two lists and returns a new list containing only the common
# elements. (without using se

def common_lists(list_1, list_2):
    result = []
    for n in list_1:
        if n in list_2:
            result.append(n)
    return result

mix_list =common_lists([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
print(mix_list)
