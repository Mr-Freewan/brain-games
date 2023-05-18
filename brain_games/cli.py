import prompt


def welcome_user() -> str:
    """
    The function asks the user to enter a name
    into the console and prints the welcome message

    :return: The name of the user in str.
    """
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    return name
