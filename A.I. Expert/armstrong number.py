n = int(input("Enter a natural number:"))
sum = 0
temp = n 
while temp > 0:
    digit = temp % 10 # extract the last digit
    sum += digit ** 3 # add the cube of the digit to the sum
    temp //= 10 # remove the last digit from the number
if sum == n:
    print(n, "is an armstrong number")
else:
    print(n, "is not an armstrong number")