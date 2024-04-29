import math
from abc import ABC

from polymorphism.shape import Shape


class RightTriangle(Shape, ABC):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = float(width)
        self.height = float(height)

    def calculate_circumference(self):
        return self.width + self.height + math.sqrt(self.width ** 2 + self.height ** 2)

    def calculate_area(self):
        return 0.5 * self.width * self.height
