import math


class Rectangle:
    def __init__(self, color, height, width):
        self.__color = str(color)
        self.__height = float(height)
        self.__width = float(width)

    @property
    def color(self):
        return self.__color

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @color.setter
    def color(self, value):
        self.color = str(value)

    @height.setter
    def height(self, value):
        if value <= 0:
            print("The height cannot be negative or 0")
            self.__height = 1
        else:
            self.__height = float(value)

    @width.setter
    def width(self, value):
        if value <= 0:
            print("The width cannot be negative or 0")
            self.__width = 1
        else:
            self.__width = float(value)

    def calculate_area(self) -> float:
        area = float(self.height * self.width)
        return area

    def print_rectangle(self):
        area = str(self.calculate_area())
        print(f"The colour of the rectangle is: {str(self.__color)}, the area of the rectangle is: {area}")


rectangle_1 = Rectangle("Green", 3, 5)
rectangle_2 = Rectangle("Orange", 5, 1)
rectangle_1.print_rectangle()
rectangle_2.print_rectangle()


class Circle:
    def __init__(self, color, radius):
        self.__color = str(color)
        self.__radius = float(radius)

    @property
    def color(self):
        return self.__color

    @property
    def radius(self):
        return self.__radius

    @color.setter
    def color(self, value):
        self.__color = str(value)

    @radius.setter
    def radius(self, value):
        if value <= 0:
            print("The value cannot be negative or 0")
            self.__radius = float(1)
        else:
            self.__radius = float(value)

    def calculate_circle_area(self) -> float:
        area = float(math.pi * (self.radius ** 2))
        return area

    def print_circle_area(self):
        area = self.calculate_circle_area()
        print(f"The circle color is: {self.color}, the area is: {str(area)}")


circle_1 = Circle("Blue", 8)
circle_2 = Circle("Red", 2)
circle_1.print_circle_area()
circle_2.print_circle_area()