# Class Exercise:
# Create a Python class representing a basic calculator with methods for addition,
# subtraction, multiplication, and division.

class Calculator:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2
    def addition(self):
        return self.number_1 + self.number_2
    def subtraction(self):
        return self.number_1 - self.number_2
    def multiplication(self):
        return self.number_1 * self.number_2
    def division(self):
        if self.number_2 == 0:
            raise Exception("The number cannot be divide by zero, Choose another number to divide by")
        return self.number_1 / self.number_2

calculator = Calculator(5,0)
print(calculator.addition())
print(calculator.subtraction())
print(calculator.multiplication())
print(calculator.division())