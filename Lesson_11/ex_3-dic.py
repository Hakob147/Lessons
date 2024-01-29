# Write a python function, which create a dictionary
# for given number N, where keys are numbers from
# 1 to N, and values are cubs of that numbers

def dictionary_from_N(number):
    result ={}
    for i in range(1,number+1):
        key = i
        value = i**3
        result[key] = value
    return result
print(dictionary_from_N(5))
