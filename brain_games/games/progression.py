from __future__ import annotations
import random


DESCRIPTION = 'What number is missing in the progression?'


def make_arithmetic_progression(first_number: int = 0,
                                min_step: int = 1,
                                max_step: int = 10,
                                min_len: int = 5,
                                max_len: int = 10
                                ) -> list[int, ...]:
    """
    The function generates a random arithmetic progression.

    :param first_number: First number in progression. Default is 0.
    :type first_number: int
    :param min_step: min step of progression. Default is 1.
    :type min_step: int
    :param max_step: max step of progression. Default is 10.
     Must equal min_step if you want a specific len.
    :type max_step: int
    :param min_len: The min quantity of numbers in
     the progression. Default is 5.
    :type min_len: int
    :param max_len: The max quantity of numbers in
     the progression. Default is 10. Must equal min_len
     if you want a specific len.
    :type max_len: int

    :return: Arithmetic progression in list
    :rtype: list[int, ...]
    """
    progression_len = random.randint(min_len, max_len)
    progression_step = random.randint(min_step, max_step)

    progression = [first_number, ]
    for i in range(1, progression_len):
        number = progression[i - 1] + progression_step
        progression.append(number)

    return progression


def get_question_and_answer() -> tuple[str, str]:
    """
    The function generates a question (progression) and
    correct answer to question "What number is missing
    in the progression?".

    :return: Question and correct answer to question
    :rtype: tuple[str, str]
    """
    MIN_FIRST_NUMBER = 0
    MAX_FIRST_NUMBER = 10

    first_number = random.randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)

    progression = make_arithmetic_progression(first_number)
    progression = list(map(str, progression))

    question_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[question_index]
    progression[question_index] = '..'

    question = ' '.join(progression)

    return question, correct_answer
