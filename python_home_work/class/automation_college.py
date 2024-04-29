import self


class Student:

    def __init__(self, name, city, email, age):
        self.name = name  # public
        self.city = city  # public
        self.__email = email  # private
        self.age = age  # setter

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <= 0 or value > 150:
            print("age cannot be negative")
            self.__age = 0
        else:
            self.__age = value

    def hi(self):
        print("hi " + self.name)

    def display(self):
        print(f"Name: {self.name} , City: {self.city}, Email: {self.__email}, Age: {self.__age} ")


moshe = Student("Moshe", "TA", "moshe@email.com", 200)
moshe.hi()

ronit = Student("Ronit", "Bat-Yam", "ronit@email.com", 25)
ronit.hi()
moshe.display()
ronit.display()
moshe.age = 20
print(moshe.age)
moshe.display()
