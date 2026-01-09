# list of questions
# store the answers
# randomly pick questions
# ask the questions
# see if they are correct
# keep the track of the score
# tell the user their score

import random


questions = {
    "What is the keyword to define a function in python?": "def",
    "Which data type is used to store true or false values?": "boolean",
    "What is the correct file extension for python file?": ".py",
    "Which symbol is used to comment in python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in python": "for",
    "What is the output of 2 ** 3 in python?": "8",
    "Which keyword is used to import module in python?": "import",
    "What is the result of 10 // 3 in python?": "3",
}


def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list, total_questions)

    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question} ")
        user_answer = input("Your answer: ").lower().strip()

        correct_answer = questions[question]

        if user_answer == correct_answer.lower().strip():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}. \n")

    print(f"Game Over!, Your final score is : {score}/{total_questions}")


python_trivia_game()
