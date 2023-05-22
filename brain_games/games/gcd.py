from __future__ import annotations

# import math
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(num_1: int, num_2: int) -> int:
    """
    Calculate the Greatest Common Divisor of num_1 and num_2. 
    Euclidean algorithm used.

    :param num_1: First number.
    :type num_1: int
    :param num_2: Second number.
    :type num_2: int

    :return: Greatest Common Divisor of num_1 and num_2
    :rtype: int
    """
    num_1 = abs(num_1)
    num_2 = abs(num_2)

    while num_2 > 0:
        num_1, num_2 = num_2, num_1 % num_2
    return num_1


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

    # Sumple usage, not custom
    # correct_answer = math.gcd(operand_1, operand_2)

    # Custom function usage
    correct_answer = get_gcd(operand_1, operand_2)

    return question, str(correct_answer)
