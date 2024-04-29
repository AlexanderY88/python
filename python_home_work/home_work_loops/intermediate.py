# exercise 1: input age until user enter: -1

print("exercise 1")
age = input("Enter your age ")
while int(age) != -1:
    print("Your age is ", age)
    age = input("Enter your age ")
print("end exercise 1")
print("another way of exercise 1")
# another way of exercise 1:

age = input("Enter your age ")
while True:
    if int(age) == -1:
        print("end")
        break
    else:
        print("Your age is ", age)
        age = input("Enter your age ")


# exercise 2: if age < 18, print young. If age > 65, print pensioner
print("exercise 2")
age = input("Enter your age ")
while int(age) != -1:
    if int(age) < 18:
        print("You are young")
        age = input("Enter your age ")
    elif int(age) > 65:
        print("You are pensioner")
        age = input("Enter your age ")
    else:
        print("You are adult ")
        age = input("Enter your age ")
print("end exercise 2")

print("another way of exercise 2")
age = input("Enter your age ")
while True:
    if int(age) == -1:
        print("end")
        break
    elif int(age) < 18:
        print("You are young")
        age = input("Enter your age ")
    elif int(age) > 65:
        print("You are pensioneer")
        age = input("Enter your age ")
    else:
        print("You are adult")
        age = input("Enter your age ")


# exercise 3:
print("exercise 3")
num = input("Enter a number ")
while True:
    if int(num) == -1:
        print("end")
        break
    elif int(num) % 2 == 0:
        print("The number is even")
        num = input("Enter a number ")
    else:
        print("The number is odd")
        num = input("Enter a number ")

# exercise 4:
print("exercise 4")
num = input("Enter a number ")
while True:
    if int(num) == 0:
        print("end")
        break
    else:
        sum = int(num) * int(num)
        if int(sum) > 30:
            print("The number is: ", sum)
            num = input("Enter a number ")
        else:
            print("The number less than 30")
            num = input("Enter a number ")















