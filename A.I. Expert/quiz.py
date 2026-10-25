print("Welcome to the quiz!")
print("Are you ready to play?")
print("Please answer the following questions:")
q1 = input("Question 1: What is the capital of France? a - Dehli, b - London, c-Paris, d - Rome")
answer1a =("Answer 1a: Delhi")
answer1b =("Answer 1b: London")
answer1c =("Answer 1c: paris")
answer1d =("Answer 1d: Rome")
select = input("Please enter your choice (a/b/c/d): ")
if select == 'a': 
    print("Incorrect! The correct answer is c. Paris.")
elif select == 'b':
    print("Incorrect! The correct answer is c. Paris.")
elif select == 'c':
    print("correct")
elif select == 'd':
    print("Incorrect! The correct answer is c. Paris.")
else:
    print("Invalid input")
    