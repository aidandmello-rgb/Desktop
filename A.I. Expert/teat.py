def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError("You can't divide by 0")
    return x / y
    except ValueError as ex:
    print("The Exception is:", ex)
number1 = float(input("Enter your first number: "))
number2 = float(input("enter your second number:"))
result = add(number1, number2)
result2 = subtract(number1, number2)
result3 = multiply(number1, number2)
result4 = divide(number1, number2)
print("The result of addition is:", result)
print("The result of subtraction is:", result2)
print("The result of multiplication is:", result3)
print("The result of division is:", result4)

