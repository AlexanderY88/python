
class Cat:
    # create cat
    def __init__(self, age, name, color):
        self.__age = age
        self.__name = name
        self.__color = color

    # create getters for all parameters
    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    # create setters for all parameters
    @age.setter
    def age(self, value):
        if value <= 0:
            print("age cannot be negative")
            self.__age = 0
        else:
            self.__age = value

    @name.setter
    def name(self, value):
        if value == "":
            print("The name cannot be empty")
            self.__name = "cat"
        else:
            self.__name = value

    @color.setter
    def color(self, value):
        if value == "":
            print("The color can`t be empty")
            self.__color = "color"
        else:
            self.__color = value

    # create print function
    def display(self):
        print(f"Cat`s name: {self.__name}, Cat`s color: {self.__color}, Cat`s age: {self.__age}")


# create a cat
cat_1 = Cat(3, "Snoopi", "black")
cat_2 = Cat(4, "Mitzi", "white")
cat_3 = Cat(-1, "", "", )
# printing cats
cat_1.display()
cat_2.display()
cat_3.display()
