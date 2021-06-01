class QuizBrain:

    def __init__(self, q_question_list):
        self.question_no = 0
        self.question_list = q_question_list
        self.score = 0

    def get_next_question(self):
        question = self.question_list[self.question_no]
        answer = input(f"Q.{self.question_no + 1} {question.text}  (True/False)")
        self.check_answer(answer, question.answer)
        print(f"Your Score {self.score}")
        self.question_no += 1

    def still_has_questions(self):
        if self.question_no >= len(self.question_list):
            return False
        else:
            return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Well that's correct")
            self.score += 1
        else:
            print("Well That's incorrect")
