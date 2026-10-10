a = str(input("Enter a letter: "))
print("Original string is:", a)

for i in a:
        if i.isalpha():
            print("The letter is an alphabet.")
        else:
            print("The letter is not an alphabet.")
