from __future__ import annotations

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
    OPERATIONS = ['+', '-', '*']

    operand_1 = randint(MIN_NUMBER, MAX_NUMBER)
    operand_2 = randint(MIN_NUMBER, MAX_NUMBER)
    operation = choice(OPERATIONS)

    question = f'{operand_1} {operation} {operand_2}'
    correct_answer = eval(question)

    return question, str(correct_answer)
