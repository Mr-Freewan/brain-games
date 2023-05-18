from __future__ import annotations
import random
import math


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer() -> tuple[str, str]:
    """
    The function generates two random integers in [1, 100] range and
    correct answer to question "What is the greatest common divisor of
    given numbers?".

    :return: Question and correct answer to question
    :rtype: tuple[str, str]
    """
    MIN_NUMBER = 1
    MAX_NUMBER = 100

    operand_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operand_2 = random.randint(MIN_NUMBER, MAX_NUMBER)

    question = f'{operand_1} {operand_2}'
    correct_answer = math.gcd(operand_1, operand_2)

    return question, str(correct_answer)
