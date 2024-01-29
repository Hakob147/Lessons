# Write a Python function to calculate count of each letter in string

def counter(string):
    result = {}
    for n in string:
        if n in result:
            result[n] = result[n]+1
        else:
            result[n] = 1
    return result

print(counter("hello"))