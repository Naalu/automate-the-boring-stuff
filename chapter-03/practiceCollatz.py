def collatz(number):
    while True:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        print(number)
        if number == 1:
            break


def getStartPoint():
    while True:
        try:
            return int(input("What number would you like to begin with? "))
        except ValueError:
            print("Please enter an integer")


keepGoing = "y"
while keepGoing == "y":
    num = getStartPoint()
    collatz(num)
    while True:
        keepGoing = input("Try another number? (y)es or (n)o ")
        if keepGoing not in "yn":
            print("Please type y or n")
            continue
        break
