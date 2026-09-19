amount = int(input("Enter your amount: "))
note1 = amount // 100
#leftover value

note2 = (amount % 100) // 50

note3 = ((amount % 100) % 50) // 10

print("Number of notes of 100:", note1)
print("Number of notes of 50:", note2)
print("Number of notes f 10:", note3) 