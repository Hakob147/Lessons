# class MyClass:
#     data_member = 12345
#     def data_method(self):
#         return "Hello"
# my_obj = MyClass()
# print(my_obj.data_member)
# print(my_obj.data_method())

class Dog:
    number = 0
    def __init__(self,my_breed,my_name,my_color,my_age):
        self.breed = my_breed
        self.name = my_name
        self.color = my_color
        self.age = my_age
        Dog.number += 1
    def burk (self):
        return f"burk {self.name}"
    def sit (self):
        return f"sit {self.name}"

dog1 = Dog("Tuzik","Jeko","black",2)
dog2 = Dog("Pitbull","Rex","white",1)
print(dog1.name)
print(Dog.number)
print(dog1.sit())