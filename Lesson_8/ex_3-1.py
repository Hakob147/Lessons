# Write a Python program to iterate over dictionaries using for loops and print out
# keys and values with f_string

dictionary = {"jack": 1020, "sape": 1030, "guido": 1040}
print (dictionary.values())
print (dictionary.keys())

for k, v in dictionary.items():
    print(f"Keys are {k}")
    print(f"Values are {v}")