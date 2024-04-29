from polymorphism.shape import Shape
from abc import ABC


class Rectangle(Shape, ABC):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = float(width)
        self.height = float(height)

    def calculate_circumference(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height
