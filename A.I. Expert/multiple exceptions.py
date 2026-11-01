try:
    a, b = eval(input("Enter two numbers separated by a comma: "))
    result = a / b
    print("The result of the division is:", result)
except ZeroDivisionError as ex:
    print("Division by 0 is error:", ex)
except SyntaxError as ex:
    print("comma is missing, please enter two numbers separated by a comma:", ex)
else:
    print("No exceptions")
finally:
    print("No matter what, this is always going to work")
