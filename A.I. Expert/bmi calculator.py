height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height / 100) ** 2
print("Your BMI value is:", bmi)
if bmi <= 18.4:
    print("you are underweight")
elif bmi <= 29.9:
    print("you are overweight")
elif bmi <= 39.9:
    print("you are obese")
else:
    print("you are severely obese")