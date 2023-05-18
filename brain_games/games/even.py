import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer() -> tuple[str, str]:
    """
    The function generates random integer in [1, 100] range and
    correct answer to question "Is this number even?". Answer can
    be 'yes' or 'no'

    :return: Tuple (str, str) of question and correct answer to question
    """
    number = random.randint(1, 100)
    right_answer = 'yes' if number % 2 == 0 else 'no'

    return str(number), right_answer
