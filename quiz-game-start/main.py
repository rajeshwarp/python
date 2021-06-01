from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

index = 0
quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.get_next_question()
