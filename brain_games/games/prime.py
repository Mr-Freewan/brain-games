from __future__ import annotations

import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    """
    The function checks whether a number is prime.

    :param number: First number in progression. Default is 0.
    :type number: int

    :return: True if number is prime, else return False
    :rtype: bool
    """
    if number < 2:
        return False

    for divider in range(2, number // 2 + 1):
        if number % divider == 0:
            return False

    return True


def get_question_and_answer() -> tuple[str, str]:
    """
    The function generates random integer in [1, 100] range and
    correct answer to question "Is this number prime?". Answer can
    be 'yes' or 'no'.

    :return: Question and correct answer to question
    :rtype: tuple[str, str]
    """
    MIN_NUMBER = 1
    MAX_NUMBER = 100

    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    prime = is_prime(number)
    right_answer = 'yes' if prime else 'no'

    return str(number), right_answer
