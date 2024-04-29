
my_value = int(input("Enter the number to check in list: "))
list_1 = []
for i in range(10):
    number_in_list = int(input("Enter the number "))
    list_1.append(number_in_list)


def search_value(the_value, the_list):
    if the_value in the_list:
        print("The number " + str(my_value) + " in the list ")
        return True
    else:
        print("The number " + str(my_value) + " is not in the list ")
        return False


print(search_value(my_value, list_1))
