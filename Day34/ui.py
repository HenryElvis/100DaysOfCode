from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
            width=280,
            text="Some question text", 
            fill=THEME_COLOR, 
            font=("Arial", 20, "italic"))

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        image_right = PhotoImage(file="images/true.png")
        self.right_button = Button(image=image_right, highlightthickness=0, command=self.right_button_clicked)
        self.right_button.grid(column=0, row=2)

        image_wrong = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=image_wrong, highlightthickness=0, command=self.wrong_button_clicked)
        self.wrong_button.grid(column=1, row=2)

        self.next_question()

        self.window.mainloop()
    
    def next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            questionn_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=questionn_text)
            
            self.right_button.config(state="active")
            self.wrong_button.config(state="active")
    
    def wrong_button_clicked(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def right_button_clicked(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.right_button.config(state="disabled")
        self.wrong_button.config(state="disabled")

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.next_question)