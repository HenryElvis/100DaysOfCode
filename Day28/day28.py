from cgitb import text
from tkinter import *
from time import sleep
from math import floor

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

rep = 0
timer = None
is_pomodoro_start = False

def checking_start():
    global is_pomodoro_start
    
    if is_pomodoro_start:
        return
    else:
        is_pomodoro_start = True
        start()

def start():
    global rep

    rep += 1

    if rep % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN)
    elif rep % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN)

def reset():
    global is_pomodoro_start

    if not is_pomodoro_start:
        return
    
    window.after_cancel(timer)
    checkmark_label.config(text="")
    timer_label.config(text="Timer")
    canvas.itemconfig(canvas_timer, text="00:00")
    global rep
    rep = 0
    is_pomodoro_start = False

def count_down(count):
    min = count // 60
    sec = count % 60

    if min < 10:
        min = f"0{min}"

    if sec < 10:
        sec = f"0{sec}"
    
    canvas.itemconfig(canvas_timer, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start()
        marks = ""
        work_session = rep // 2
        for _ in range(work_session):
            marks += "✓"
        checkmark_label.config(text=marks)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
canvas_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checkmark_label.grid(column=1, row=3)

start_button = Button(text="Start", highlightthickness=0, command=checking_start)
reset_button = Button(text="Reset", highlightthickness=0, command=reset)

start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

window.mainloop()