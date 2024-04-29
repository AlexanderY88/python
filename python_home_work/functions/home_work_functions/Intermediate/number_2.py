# function that accepts 10 variables of type int and returns the minimum number


def min_number(variables) -> str:
    my_variables = []
    for i in range(10):
        user_input = int(input("Enter an int number: "))
        my_variables.append(user_input)
    minimum_element = min(my_variables)
    min_element = str("The minimum number is " + str(minimum_element))
    return min_element


print(min_number(list))








