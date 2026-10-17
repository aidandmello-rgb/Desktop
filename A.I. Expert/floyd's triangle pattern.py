print("Floyd's triangle pattern")
n = int(input("Enter the number of rows: "))
m = 1
for i in range(n):
    for j in range(i + 1):
        print(m, end=" ")
        m = m + 1
    print()