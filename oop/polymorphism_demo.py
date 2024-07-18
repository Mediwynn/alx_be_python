class Shape:
    def __init__(self) -> None:
        pass
    
    def area(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
        super().__init__()
    
    
    def area(self):
        Shape.area = self.length * self.width
        
        return str(super().area())


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
        super().__init__()
    
    def area(self):
        
        Shape.area = math.pi * self.radius * self.radius

        return str(super().area())