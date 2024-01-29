# Write an abstract class with name GeometricFigure
# Write 2 geometric figure classes by inheriting from GeometricFigure
# Write 2 functions
# get_perimeter -> return perimeter of figure
# get_area -> return area of figure

from abc import ABC, abstractmethod
class GeometricFigure(ABC):
    def get_perimeter(self):
        pass
    def get_area(self):
        pass

class Quadrat(GeometricFigure):
    def __init__(self, side):
        self.side = side
    def get_perimeter(self):
        return 4 * self.side
    def get_area(self):
        return self.side ** 2


class Rectangle(GeometricFigure):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def get_perimeter(self):
        return 2 *(self.width + self.length)
    def get_area(self):
        return self.width * self.length

quadrat = Quadrat(5)
rectangle = Rectangle(4,6)

print(quadrat.get_area())
print(quadrat.get_perimeter())

print(rectangle.get_area())
print(rectangle.get_perimeter())