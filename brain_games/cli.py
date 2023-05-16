import prompt


def welcome_user() -> None:
    """
    The function asks the user to enter a name in the console and prints a greeting
    """
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
