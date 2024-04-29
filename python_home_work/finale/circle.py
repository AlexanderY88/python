import math
from abc import ABC
from polymorphism.shape import Shape


class Circle(Shape, ABC):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = float(radius)

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius
