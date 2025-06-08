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

    bulls = 0
    cows = 0

    unmatched_secret = []
    unmatched_guess = []
    
    for i in range(4):
        if secret_code[i] == player_guess[i]:
            bulls+=1
        else:
            unmatched_secret.append(secret_code[i])
            unmatched_guess.append(player_guess[i])
    
    for digit in unmatched_guess:
        if digit in unmatched_secret:
            cows += 1
            unmatched_secret.remove(digit)
    
    return bulls, cows