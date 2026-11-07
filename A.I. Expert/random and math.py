import random
number = str(random.randint(1,11))
playing = True

print("I am going to generate a number between 1 and 10, you have to guess it.")
while playing:
    guess = input("what is your guess?")

    if guess == number:
        print("Guess is correct!!")
        playing = False
        break

    else:
        print("Guess is wrong!! Try again")
    


