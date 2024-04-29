class Rectangle:
    def __init__(self, area, color):
        self.__area = float(area)
        self.__color = str(color)

    @property
    def area(self):
        return self.area

    @property
    def color(self):
        return self.color

    @area.setter
    def area(self, value):
        self.__area = float(value)

    @color.setter
    def color(self, value):
        self.__color = str(value)

    def print_rectangle(self):
        print(f"The rectangle area: {self.__area}, rectangle color: {self.__color}")


class Circle:
    def __init__(self, area, color):
        self.__area = float(area)
        self.__color = str(color)

    @property
    def area(self):
        return self.area

    @property
    def color(self):
        return self.color

    @area.setter
    def area(self, value):
        self.__area = float(value)

    @color.setter
    def color(self, value):
        self.__color = str(value)

    def print_circle(self):
        print(f"The circle area: {self.__area}, the circle color: {self.__color}")


rectangle_1 = Rectangle(15.5, "green")
rectangle_1.print_rectangle()

circle_1 = Circle(22.07, "blue")
circle_1.print_circle()
