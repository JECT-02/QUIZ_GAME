class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

def run_quiz():
    quiz = Quiz()
    from question import Question

    q1 = Question("¿Cuál es la capital de Francia?", ["París", "Madrid", "Lima", "Roma"], "París")
    q2 = Question("¿Cuánto es 2 + 2?", ["3", "4", "5", "6"], "4")

    quiz.add_question(q1)
    quiz.add_question(q2)

    while True:
        question = quiz.get_next_question()
        if not question:
            break
        print(question.prompt)
        for i, option in enumerate(question.options):
            print(f"{i + 1}. {option}")
        print()