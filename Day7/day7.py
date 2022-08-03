import random
import hangman_art
import hangman_words

random_index = random.randint(0, len(hangman_words.word_list) -1)
word = hangman_words.word_list[random_index]

print(word)
display = []

for i in word:
	display.append("_")

lives = 6
word_guessed = []
end_game = False

print(hangman_art.logo)

while not end_game:
	letter = input("Guess a letter - ").lower()
	
	if letter not in word:
		if letter not in word_guessed:
			lives -= 1
			word_guessed.append(letter)
			print(f"You guessed {letter}, that's not in the word. You lose a life.")
			print(hangman_art.stages[lives])
			
			if lives == 0:
				end_game = True
				print("You Loose!")
		else:
			print(f"You've already guessed {letter}")
	else:
		if letter not in word_guessed:
			for i in range(len(word)):
				if word[i] == letter:
					display[i] = letter
			word_guessed.append(letter)
		else:
			print(f"You've already guessed {letter}.")

		print(display)
	
		if "_" not in display:
			end_game = True
			print("You Win!")