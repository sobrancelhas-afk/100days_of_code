class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
    
    def next_question(self):
        self.current_q = self.question_list[self.question_number]
        self.question_number += 1
        self.user_answer = input(f"{self.question_number}. {self.current_q.text}: (True/False?): ")        

    def check_answer(self):

        if self.user_answer.lower() == self.current_q.answer.lower():
            print(f"you are goddamn right")
            self.score += 1
        else:
            print("errou feio")
        print(f"Current Score = {self.score} / {self.question_number}\n")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

        
