def add(P, Q):
    return P+Q
def subtract(P, Q):
    return P-Q
def multiply(P, Q):
    return P*Q
def divide(P, Q):
    return P/Q

print("Select the operation you want to use: ")
print("a. add")
print("b. subtract")
print("c. multiply")
print("d. divide")

select = input("Please enter your choice (a/b/c/d): ")

P = float(input("Enter your first number: "))
Q = float(input("Enter your second number: "))

if select == 'a':
    print(P, "+", Q, "=", add(P, Q))
elif select == 'b':
    print(P, "-", Q, "=", subtract(P, Q))
elif select == 'c':
    print(P, "*", Q, "=", multiply(P, Q))
elif select == 'd':
    print(P, "/", Q, "=", divide(P, Q))
else:
    print("invalid input")