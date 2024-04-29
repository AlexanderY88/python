class Cat:
    # create cat
    def __init__(self, name, color, age):
        self.__age = age
        self.__color = color
        self.__name = name

    # getters for all parameters
    @property
    def age(self):
        return self.__age

    @property
    def color(self):
        return self.__color

    @property
    def name(self):
        return self.__name

    # setters for all parameters
    @color.setter
    def color(self, value):
        if value == "":
            print("The color cannot pe empty")
            self.__color = "color"
        else:
            self.__color = str(value)

    @name.setter
    def name(self, value):
        if value == "":
            print("The name cannot pe empty")
            self.__name = "cat"
        else:
            self.__name = value

    @age.setter
    def age(self, value):
        if int(value) < 0:
            print("The age cannot be negative")
            self.__age = 0
        else:
            self.__age = value


# function, prints all cats details of all cats in list my_cats
def all_cats_details():
    for i in range(len(my_cats)):
        cat = my_cats[i]
        print(f"cat_{i + 1}: Name: {cat.name}, Color: {cat.color}, {cat.age} years old")


def cat_details_by_name(name):
    for i in range(len(my_cats)):
        if name == my_cats[i].name:
            cat = my_cats[i]
            print(f"cat_{i + 1}: Name: {cat.name}, Color: {cat.color}, {cat.age} years old")


my_cats = [
    Cat("Snooppy", "Black", 3),
    Cat("Mitzi", "White", 2),
    Cat("Kitty", "Orange", 1),
    Cat("Choco", "Brown", 6),
    Cat("Loo loo", "White", 4)
]

for i in range(len(my_cats)):
    cat = my_cats[i]
    # print(f"cat_{i + 1}: Name: {cat.name}, Color:  {cat.color}, {cat.age} years old")

all_cats_details()
print()
cat_details_by_name("Mitzi")
print()
cat_details_by_name("Choco")
