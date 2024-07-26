from data import fetch_questions, fetch_categories
from question_model import Question
from quiz_brain import QuizBrain
import html


def get_user_input():
    amount = int(input("How many questions would you like? "))

    categories = fetch_categories()
    print("\nSelect a category:")
    for category in categories:
        print(f"{category['id']}: {category['name']}")

    category = input("\nEnter the category number: ")
    difficulty = input("Choose the difficulty (easy, medium, hard): ").lower()
    question_type = 'boolean'  
    return amount, category, difficulty, question_type

def main():
    amount, category, difficulty, question_type = get_user_input()
    question_data = fetch_questions(amount, category, difficulty, question_type)

    question_bank = []
    print("\n")
    for question in question_data:
        question_text = html.unescape(question['question'])
        question_answer = html.unescape(question['correct_answer'])
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_num}")

if __name__ == "__main__":
    main()