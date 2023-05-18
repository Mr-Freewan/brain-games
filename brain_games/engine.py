from __future__ import annotations
from types import ModuleType

from brain_games.cli import welcome_user
import prompt


MAX_SUCCESSFUL_ATTEMPTS = 3


def process_game(game: ModuleType | object) -> None:
    """
    The function starts the question-and-answer game.

    :param game: module or class, which consists rules
                 and generates question and right answer.

                 The argument must contain within itself:
                 - a DESCRIPTION: str variable or attribute of class.
                 It must contains game rules
                 - a get_question_and_answer() -> tuple[str, str]
                 function or method. The function must generate
                 question and correct answer to this question
                 and returns it by tuple [question, correct_answer].
    :type game: ModuleType | object
    """
    user_name = welcome_user()  # Welcome user and get user's name
    print(game.DESCRIPTION)  # Print game description (rules)

    attempt = 0
    while attempt < MAX_SUCCESSFUL_ATTEMPTS:
        question, correct_answer = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        # If answer is wrong - stop the program:
        if not (user_answer == correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {user_name}!")
            return  # Stop the program

        #  If answer correct - send next question
        print('Correct!')
        attempt += 1

    print(f'Congratulations, {user_name}!')
