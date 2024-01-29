# Write a python function, which add a new value with given key in dict

def add_dict(dict,key,value):
    dict[key] = value

dic_1= {"name": "John", "age": 25}
add_dict(dic_1,"e-mail","John@gmail.com")
print(dic_1)
