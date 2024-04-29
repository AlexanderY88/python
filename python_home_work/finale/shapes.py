from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def calculate_circumference(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


