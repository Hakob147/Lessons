# Write an abstract class with name Employee
# Write 2 employee classes by inheriting from abstract Employee
# Write function
# get_info -> return string with name and position
# calculate_salary -> return float with information about employee salary


from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def get_info(self):
        pass
    def calculate_salary(self):
        pass

class Accountant(Employee):
    def __init__(self, name, position, salary):
        super().__init__(name, position)
        self.salary = salary
    def get_info(self):
        return f"Name = {self.name}, Position = {self.position}"
    def calculate_salary(self):
        return f"Salary is {self.salary}"

class Manager(Employee):
    def __init__(self, name, position, salary):
        super().__init__(name, position)
        self.salary = salary
    def get_info(self):
        return f"Name = {self.name}, Position = {self.position}"
    def calculate_salary(self):
        return f"Salary is {self.salary}"

accountant = Accountant("John", "accountant", "500,000")
manager = Manager("Jim", "manager", "800,000")

print(accountant.get_info())
print(accountant.calculate_salary())

print(manager.get_info())
print(manager.calculate_salary())