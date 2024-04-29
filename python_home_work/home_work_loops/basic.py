# exercise 1: print with while loop numbers from 1 to 99
num = 1
while num < 100:
    print(num, end=", ")
    num += 1

print()

# exercise 2: print numbers from 1 to 99 with for loop
for i in range (1, 100, 1):
    print(i, end=", ")

print()

# exercise 3: loop thet prints all even numbers from 2 to 22
for i in range (1, 23, 1):
    if i % 2 == 0:
        print(i, end=", ")

print()

# exercise 4: loop that prints all odd numbers from 11 to 101
for i in range (10, 102, 1):
    if i % 2 == 1:
        print(i, end=", ")

