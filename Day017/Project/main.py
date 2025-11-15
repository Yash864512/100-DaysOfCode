from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # To store object to each question

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    '''Creating a Question object using constructor, by extracting text and answer from each
    dictionary in question_data list'''
    question_bank.append(new_question)  # Appending or adding the object at the end of the question_bank list

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz!")
print(f"The final score is: {quiz.score}/{quiz.question_no}")
