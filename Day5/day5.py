import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

number_letters = int(input("How many letters would you like in your password ? - "))
number_symbols = int(input("How many symbols would you like ? - "))
number_numbers = int(input("How many numbers would you like ? - "))

password = ""

for i in range(1, number_letters +1):
	password += letters[random.randint(0, len(letters))]

for i in range(1, number_numbers +1):
	password += numbers[random.randint(0, len(numbers))]

for i in range(1, number_symbols +1):
	password += symbols[random.randint(0, len(symbols))]

l = list(password)
random.shuffle(l)

password = ''.join(l)

print(password)