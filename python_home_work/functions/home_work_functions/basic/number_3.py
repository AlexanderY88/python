# function recive number and print the number + 5
my_value = 0


def calc_value(value) -> str:
    num = int(input("Enter a number "))
    my_num = num + 5
    message = str("Your number is: " + str(num)) + " + 5 = " + str(my_num)
    return message


print(calc_value(my_value))
