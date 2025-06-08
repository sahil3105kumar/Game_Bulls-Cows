import random

def generate_secret_code():
    """
    Generates a secret code based on settings in config.py.
    Duplicates are allowed as per the original example.
    Returns a list of strings (digits).
    """
    code=[]
    for i in range(4):
        single_digit = random.randint(0,9)
        code.append(str(single_digit))

    return code




def calculate_feedback(secret_code, player_guess):
    """
    Calculates the number of bulls and cows for a given guess.
    - secret_code: The list of strings representing the secret code.
    - player_guess: The list of strings representing the player's guess.
    Returns a tuple: (bulls, cows)
    """

    