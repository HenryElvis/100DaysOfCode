class Quiz:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {current_question.text} (True/False): ")
        self.checking_result(user_answer, current_question.answer)

    def checking_result(self, answer, result):
        if answer.lower() == result.lower():
            self.score += 1
            print("You got it right !")
        else:
            print("That's wrong.")
            print(f"The correct answer was : {result}.")

        print(f"Your current score is: {self.score}/{self.question_number}.")

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def end_of_quiz(self):
        print("You've completed the quiz")
        print(f"Your final score was : {self.score}/{len(self.question_list)}")