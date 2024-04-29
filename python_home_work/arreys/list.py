# arreys

grades = [90, 93, 97, 100]
print(grades)
# print(type(grades))
# grades[0] = 80
# print(grades)
# print(grades[2])

sum = 0
for grade in grades:
    print(grade, end=" , ")
    sum += grade
print()
print("sum ",sum)
print("average: ", sum / len(grades))

# how to add elements to list:
# first way: append
print("Add element via \"append\" ")
print("original list")
print(grades)
grades.append(97)
print(grades)

# another way is via new_elements' when you concat two lists:
new_elements = [92, 99]
print("add new elements: ", new_elements)
grades = grades + new_elements
print(grades)

# more ways: it`s possible to extend:
new_elements2 = [88, 77]
print("existing elements in grades: ", grades)
print("another way to add elements via extend, adding this to elements: ", new_elements2)
grades.extend(new_elements2)
print("the grades list is now: ", grades)

# there is a more way to add element to list: Using list comprehension
print("The grades list is now: ", grades)
new_elements3 = [91, 88, 100, 100]
print("add new elements to the list: ", new_elements3)
grades += new_elements3
print("Now the list grades is: ", grades)

# some ways to delete element from list:
# first way is using: remove . It removes the value and not by element index in list. For example:
# we want to delete grade 92 but we don`t know the index
print("Existing grades list is:  ", grades)
grades.remove(92)
print("After removing element with value = 92: ", grades)
# If there are more elements with the same value in the list' like grade 88, it will delete first element with 88
grades.remove(88)
print("After removing FIRST element with value = 88: ", grades)

# removing element by itws index in list:
print("Existing grades list is:  ", grades)
del grades[2]
print("It will delete element with index = 2, the grade 97 in the list: ", grades)

# one more way is pop method with index

my_list = [1, 2, 3, 4, 5]
print("The new list is: ", my_list)
removed_element = my_list.pop(2)
print(my_list)  # Output: [1, 2, 4, 5]
print("Removed Element:", removed_element)

# the last way is more complicated. Using list comprehension:
my_list2 = [1, 2, 3, 4, 5]
print("New list 2 is: ", my_list2 )
my_list2 = [x for x in my_list if x != 5]
print("New list 2 is", my_list2)  # Output: [1, 2, 3, 4]
print("Removed Element:", removed_element)
