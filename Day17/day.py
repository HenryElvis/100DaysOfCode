from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_bank = []

for d in question_data:
    question = Question(d["question"], d["correct_answer"])
    question_bank.append(question)

quiz = Quiz(q_list=question_bank)

while quiz.still_has_question():
    quiz.next_question()

quiz.end_of_quiz()