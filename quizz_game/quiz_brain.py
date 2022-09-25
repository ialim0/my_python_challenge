class QuizBrain:
    def __init__(self, question_list):
        self.n = 0
        self.n_question = 0
        self.question_list = question_list

        # method to display next question

    def next_question(self):
        current_question = self.question_list[self.n_question]
        u_answer = input(f"Q.{self.n_question + 1} {current_question.text} (True or False):").lower()

        self.check(u_answer, current_question.answer)
        self.n_question = self.n_question + 1  # to browse the list of question

    def still_have_question(self):
        return self.n_question < len(self.question_list)

    def check(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.n = self.n + 1
        else:
            print(f'The correct answer is :{correct_answer}')

    def end(self):
        print(f"Your score is : {self.n}/{len(self.question_list)}")
