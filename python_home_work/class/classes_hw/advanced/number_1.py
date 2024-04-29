class Student:
    def __init__(self, name, email, city, age, lastname, the_student_grades):
        self.__the_student_grades = the_student_grades
        self.__name = name
        self.__email = email
        self.__city = city
        self.__age = age
        self.__lastname = lastname

    # getters
    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def city(self):
        return self.__city

    @property
    def age(self):
        return self.__age

    @property
    def lastname(self):
        return self.__lastname

    @property
    def the_student_grades(self):
        return self.__the_student_grades

    # setters:
    @name.setter
    def name(self, value):
        if value == "":
            print("The first name cannot be empty")
            self.__name = "Firstname"
        else:
            self.__name = str(value)

    @email.setter
    def email(self, value):
        if value == "":
            print("The email can't be empty ")
            self.__email = "email"
        elif "@" in value:
            self.__email = str(value)
        else:
            print("The email is not correct ")
            self.__email = "email"

    @city.setter
    def city(self, value):
        if value == "":
            print("The city cannot be empty ")
            self.__city = str("city")
        else:
            self.__city = str(value)

    @age.setter
    def age(self, value):
        if value <= 0:
            print("Age cannot be negative ")
            self.__age = int(0)
        else:
            self.__age = value

    @lastname.setter
    def lastname(self, value):
        if value == "":
            print("The lastname cannot be empty ")
            self.__lastname = str("Lastname")
        else:
            self.__lastname = str(value)

    @the_student_grades.setter
    def the_student_grades(self, value):
        if value is None:
            print("The grades cannot be empty ")
            self.__the_student_grades = [0]
        else:
            self.__the_student_grades = list(value)  # list

    # creating print function with: __repr__
    def __repr__(self):
        return f"Student name: {self.name}, email: {self.email}, city: {self.city}, age: {self.age}, lastname: {self.lastname}, grades: {self.__the_student_grades}"

    # def student_details(self): print(f"Student name: {self.name}, email: {self.email}, city: {self.city},
    # age: {self.age}, lastname: {self.lastname}, grades: {self.__the_student_grades}")

    def student_average_grade(self):
        sum = 0
        for i in range(len(self.the_student_grades)):
            sum += self.the_student_grades[i]
        average = sum / (len(self.__the_student_grades) + 1)
        return average

    # print average of one student
    def print_student_average(self):
        print("The student`s average is: ", self.student_average_grade())


# calculates the average of grades from the students list one by one
def one_by_one_students_average():
    list_of_averages = []
    for i in range(len(students)):
        sum_grades = sum(students[i].the_student_grades)
        student_average = sum_grades / len(students[i].the_student_grades)
        list_of_averages.append(float(student_average))
    return list_of_averages


# prints the average of grades from the students list one by one using function: one_by_one_students_average(list)
def print_student_average():
    list_of_averages = one_by_one_students_average()
    for i in range(len(list_of_averages)):
        print("The average of the student " + str(students[i].name) + ": " + str(list_of_averages[i]))


# calculates and prints the average of all students in list
def average_of_all_students():
    list_of_averages = one_by_one_students_average()
    average = sum(list_of_averages)/len(list_of_averages)
    return average

def print_average_of_all_students():
    average = average_of_all_students()
    print("The average of all students is: ", average)



# create 5 students
students = [
    Student("Moshe", "moshe@mail.com", "Bat-Yam", 25, "Cohen", [100, 95, 97, 90, 98]),
    Student("Izik", "itzik@mail.com", "Holon", 27, "Pinti", [88, 75, 90, 92, 90, 99]),
    Student("Galit", "galit@mail.com", "Tel-Aviv", 26, "Levi", [100, 95, 97, 100, 100]),
    Student("Avraham", "abrasha@mail.com", "Or Yehuda", 31, "Abramov", [89, 78, 90, 77, 95, 97]),
    Student("Miri", "miri@mail.com", "Rishon leZion", 24, "Klayn", [89, 78, 90, 77, 95, 97])
]
# print 5 students via __repr__ function
print(students[0])
print(students[1])
print(students[2])
print(students[3])
print(students[4])

# print average grade
## students[2].print_student_average() students[0].print_student_average()
# # students[1].print_student_average()
# students[3].print_student_average()
# students[4].print_student_average()

# print all students average one by one
one_by_one_students_average()
print_student_average()
print_average_of_all_students()
