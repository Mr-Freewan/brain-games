from __future__ import annotations

import random


DESCRIPTION = 'What number is missing in the progression?'


def make_arithmetic_progression(first_number: int = 0,
                                step: int = 1,
                                length: int = 5
                                ) -> list[int, ...]:
    """
    The function generates a random arithmetic progression.

    :param first_number: First number in progression. Default is 0.
    :type first_number: int
    :param step: Step of progression. Default is 1.
    :type step: int
    :param length: Length of progression. Default is 5.
    :type length: int

    :return: Arithmetic progression in list
    :rtype: list[int, ...]
    """
    progression = [first_number, ]
    for i in range(1, length):
        number = progression[i - 1] + step
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
    MIN_STEP = 1
    MAX_STEP = 10
    MIN_LENGTH = 5
    MAX_LENGTH = 10

    first_number = random.randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
    progression_len = random.randint(MIN_LENGTH, MAX_LENGTH)
    progression_step = random.randint(MIN_STEP, MAX_STEP)

    progression = make_arithmetic_progression(first_number=first_number,
                                              length=progression_len,
                                              step=progression_step)
    progression = list(map(str, progression))

    skip_component_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[skip_component_index]
    progression[skip_component_index] = '..'

    question = ' '.join(progression)

    return question, correct_answer
