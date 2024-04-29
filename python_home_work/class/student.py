class Student:

    def __init__(self, name, address, age, email):
        self.name = name
        self.address = address
        self.age = age
        self.email = email


    def display(self):
        print(f"Name: {self.name}")
        print(f"Adress: {self.address}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

