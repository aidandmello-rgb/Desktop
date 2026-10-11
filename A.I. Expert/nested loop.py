string = input("Enter a string: ")
char = input("Enter a character to check: ")
i = 0 # initializing the index variable
count = 0 # counting the occurance of the character
while i < len(string):
    if string[i] == char:
        count = count + 1
    i = i + 1
print("the character", char, "occurs", count, "times in the string.")