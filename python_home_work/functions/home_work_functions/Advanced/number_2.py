from typing import Tuple

numbers = []
for i in range(5):
    num = input("Please enter a number ")
    numbers.append(float(num))

print("Your numbers are: ", numbers, " ,")


# function that finds the maximal number in the list
def max_number(the_list):
    max_num = max(the_list)
    print("The maximal number is: ", max_num)


# function that check`s minimum number
def min_number(the_list):
    min_num = min(the_list)
    print("The minimal number is: ", min_num)


# function: sum of all numbers
def sum_numbers(the_list) -> tuple[str, float]:
    sum_number = sum(the_list)
    sum_of_numbers = "The sum of numbers is: ", sum_number
    return sum_of_numbers


# function average of the numbers
def average_numbers(the_list) -> tuple[str, float]:
    sum_of_the_list = int(sum(the_list))
    average = int(sum_of_the_list) / len(the_list)
    average_message = "The average of the numbers is: ", average
    return average_message


max_number(numbers)
min_number(numbers)
print(sum_numbers(numbers))
print(average_numbers(numbers))
