from abc import ABC
from polymorphism.shape import Shape


class Square(Shape, ABC):
    def __init__(self, color, width):
        super().__init__(color)
        self.width = float(width)

    def calculate_circumference(self):
        return self.width * 4

    def calculate_area(self):
        return self.width * self.width
