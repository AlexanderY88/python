while True:
    num = int(input("Enter a number between 0 and 100: "))

    if num < 2:
        print("The number ", num, " is prime ")
    else:
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break

        if prime:
            print("The number ", num, " is prime ")
        else:
            print("The number is not prime ")

