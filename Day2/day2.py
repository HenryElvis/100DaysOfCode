# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

days, weeks, months = 0, 0, 0

leftYears = 90 - int(age)

days = leftYears * 365
weeks = leftYears * 52
months = leftYears * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")