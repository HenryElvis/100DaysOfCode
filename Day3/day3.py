print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 ''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
way = input("Choose your way, left or right ? l or r ? - ")

if way == 'r' or way == "right":
	print("Wrong way.\nThis is a game over.")
elif way == 'l' or way == "left":
	print("Good choice !")
	
	choice = input("Now in front of you, a river what you decided ? Wait or Swim ? w or s ? - ")
	if choice == 'w' or "Wait":
		print("Nice choice !")
		
		door = input("Now the last choice to make\nWhich door do you choose ? Blue ? Red ? Yellow ? b, r or y - ")
	
		if door == "Red" or door == 'r':

			print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[https://ascii.co.uk/art]
*******************************************************************************''')
			print("\n\nVery Good ! You find it !\nEnjoy your treasure and see you!")
		elif door == "Blue" or door == 'b' or door == "Yellow" or door == 'y':
			print("Oh no you choose the bad door !\nSorry but it's game over !")
		else:
			quit()

	elif choice == 's' or "Swim":
		print("Wrong way.\nThis is a game over.")
	else:
		quit()
else:
	quit()