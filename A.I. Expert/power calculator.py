n = float(input("Enter number whose power is to be calculated: "))
m = float(input("Enter the power: "))
for i in range(1, int(m)+1):
    power = n ** i
    print(n, "raised to the power", i, "is:", power)
