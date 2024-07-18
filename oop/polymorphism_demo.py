import math

class Shape:
    def area(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
        super().__init__()
    
    
    def area(self):
        Shape.area = self.length * self.width
        
        return Shape.area


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
        super().__init__()
    
    def area(self):
        
        Shape.area = math.pi * self.radius** 2

        return Shape.area