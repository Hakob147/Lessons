# Write a python program which concat 2 dicts

def concat(dic_1,dic_2):
    result = {**dic_1,**dic_2}
    return result
print(concat({"a":1,"b":2},{"c":3,"d":4}))