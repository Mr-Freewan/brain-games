from __future__ import annotations

import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer() -> tuple[str, str]:
    """
    The function generates random integer in [1, 100] range and
    correct answer to question "Is this number even?". Answer can
    be 'yes' or 'no'.

    :return: Question and correct answer to question
    :rtype: tuple[str, str]
    """
    MIN_NUMBER = 1
    MAX_NUMBER = 100

    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    right_answer = 'yes' if number % 2 == 0 else 'no'

    return str(number), right_answer
