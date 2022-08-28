from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    data_dict = data.to_dict(orient="records").copy()
    word_to_learn = data_dict.copy()

current_card = {}

def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    current_card = choice(word_to_learn)
    canvas.itemconfig(card_image, image=old_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_image, image=new_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def correct_button():
    global word_to_learn

    if len(word_to_learn) <= 1:
        word_to_learn = data_dict.copy()
    else:
        word_to_learn.remove(current_card)
        new_data = pandas.DataFrame(word_to_learn)
        new_data.to_csv("data/words_to_learn.csv")
    
    next_card()

def incorrect_button():
    next_card()

window = Tk()

window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, heigh=526)
old_image = PhotoImage(file="images/card_front.png")
new_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=old_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Aiel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Aiel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

wrong_PhotoImage = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_PhotoImage, highlightthickness=0, command=incorrect_button)
wrong_button.grid(column=0, row=1)

right_PhotoImage = PhotoImage(file="images/right.png")
right_button = Button(image=right_PhotoImage, highlightthickness=0, command=correct_button)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()