# Write a python function which create dict from 2 lists with the same length

def dic_from_two_lists(list_1,list_2):
    result ={}
    for i in range(len(list_1)):
        result[list_1[i]] = list_2[i]
    return result

a=dic_from_two_lists(["a","b","c"],[1,2,3])
print(a)
