from typing import Tuple

from inheritance_hw.num_1.person import Person


class Student(Person):
    def __init__(self, name, email, course_name, active):
        super().__init__(name, email)
        self.course_name = str(course_name)
        self.active = bool(active)

    def print_info_details(self) -> str:
        details = f"{super().print_info()}, Course name: {self.course_name}, is active: {str(self.active)}"
        return details

    def print_info(self):
        print(self.print_info_details())


moshe = Student("Moshe", "moshe@mail.com", "automation python", True)
sarah = Student("Sarah", "sarah@gmail.com", "Java", True)
tal = Student("Tal", "tal@gmail.com", "Postman", False)

moshe.print_info()
sarah.print_info()
tal.print_info()
