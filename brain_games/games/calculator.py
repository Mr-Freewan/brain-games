from __future__ import annotations

from operator import add, mul, sub
from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer() -> tuple[str, str]:
    """
    The function generates a random mathematical expression
    (+, - or *) with two random operands and correct answer to expression.

    :return: Question and correct answer to question
    :rtype: tuple[str, str]
    """
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    OPERATIONS = [(add, '+'), (sub, '-'), (mul, '*')]

    operand_1 = randint(MIN_NUMBER, MAX_NUMBER)
    operand_2 = randint(MIN_NUMBER, MAX_NUMBER)
    operation, operator = choice(OPERATIONS)

    question = f'{operand_1} {operator} {operand_2}'
    correct_answer = operation(operand_1, operand_2)

    return question, str(correct_answer)
