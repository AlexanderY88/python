list_1 = [1, 2, 4]
list_2 = [1, 2, 3]


def compare_lists(list_1, list_2) -> bool:
    if len(list_1) == len(list_2):
        for i in range(len(list_1)):
            if list_1[i] != list_2[i]:
                print("The variable number " + str(i) + " is not the same at two lists")
                return False
        print("The lists are the same")
        return True
    else:
        print("The length of list_1 is not the same length as list_2")
        return False


compare_lists(list_1, list_2)
