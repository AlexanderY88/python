# calculating method
def calculate_sum(number1, number2) -> int:
    my_sum = number1 + number2
    # print(str(number1) + " + " + str(number2) + " = " + str(my_sum))
    return my_sum


# calculate_sum(10, 15)
# calculate_sum(50, 200)
# calculate_sum(300, 600)
a = calculate_sum(100, 200) + calculate_sum(400, 51)
print(a)
b = calculate_sum(calculate_sum(100, 200), calculate_sum(300, 400))
print(b)