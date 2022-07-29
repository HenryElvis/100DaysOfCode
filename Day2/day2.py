print("Welcome to the tip calculator")
total = input("What was total bill ? ")
tip = input("What percentage tip would you like to give ? 10, 12, or 15 ? ")
peopleNumber = input("How many people to split the bill ? ")

pay = (float(total) * (1 + float(tip) / 100)) / int(peopleNumber)
pay = round(pay, 2)

print(f"Each person should pay : ${pay}")