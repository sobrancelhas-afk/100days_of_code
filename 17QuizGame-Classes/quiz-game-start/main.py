from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

data = question_data

question_bank = []
for i in data:
    question_bank.append(Question(i["question"],i["correct_answer"]))

brain = QuizBrain(question_bank)

while brain.still_has_questions():
    brain.next_question()
    brain.check_answer()
print(f"Quiz ended!\nFinal Score: {brain.score} / {brain.question_number}")