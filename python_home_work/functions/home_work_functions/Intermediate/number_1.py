# function that accepts 3 variables of type int and returns the minimum number

def min_number() -> str:
    num1 = input("Enter first number ")
    num2 = input("Enter first number ")
    num3 = input("Enter first number ")
    minimum = min(num1, num2, num3)
    the_answer = ("The minimum number is: " + str(minimum))
    return the_answer


print(min_number())
