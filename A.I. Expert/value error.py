try:
    number = int(input("Enter a number: "))
    print("Your number is:", number)
except ValueError as ex:
    print("Exception:", ex)
