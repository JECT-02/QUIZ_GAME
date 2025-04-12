from trivia import Quiz
from Question import Question

def test_quiz_scoring():
    quiz = Quiz()
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    quiz.add_question(question)
    assert quiz.answer_question(question, "4") == True
    assert quiz.correct_answers == 1
    assert quiz.incorrect_answers == 0
