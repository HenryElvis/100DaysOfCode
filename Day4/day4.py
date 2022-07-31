rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

choice = input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors. - ")

if choice == '0':
	print(rock)
elif choice == '1':
	print(paper)
elif choice == '2':
	print(scissors)
else:
	quit()

print("Computer chose:\n")

computerChoice = random.randint(0, 2)

if computerChoice == 0:
	print(rock)

	if choice == '0':
		print("Drew")
	elif choice == '1':
		print("You win !")
	else:
		print("You lose !")

elif computerChoice == 1:
	print(paper)

	if choice == '0':
		print("You lose !")
	elif choice == '1':
		print("Drew !")
	else:
		print("You win !")

elif computerChoice == 2:
	print(scissors)

	if choice == '0':
		print("You win !")
	elif choice == '1':
		print("You lose !")
	else:
		print("Drew !")

else:
	quit()