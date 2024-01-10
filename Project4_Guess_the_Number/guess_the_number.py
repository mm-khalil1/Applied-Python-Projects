"""
Guess the Number
This simple console-based game allows the user to guess a randomly chosen number by the computer.
The user is prompted to input a number between 1 and 10, and the game provides feedback on whether the PC's
number is higher or lower. The game continues until the user guesses the correct number or chooses to exit.

Auther: Mahmoud Khalil
Date: 08-12-2023
"""


import random

def get_user_guess():
    """
    Get a valid user input for the guessed number within the range of 1 to 10.

    Returns:
        int: Valid user input.
    """
    user_number = 0
    while not (1 <= user_number <= 10):
        try:
            user_number = int(input("Guess the number (from 1 to 10): "))
        except ValueError:
            user_number = 0
        if 1 <= user_number <= 10:
            return user_number
        print("Invalid input. ", end="")

def compare_numbers(user, pc):
    """
    Compare the user's guessed number with the randomly generated PC number.

    Args:
        user (int): User's guessed number.
        pc (int): Randomly generated PC number.

    Returns:
        int: Number of attempts taken to guess the correct number.
    """
    attempts = 0
    while user != pc:
        attempts += 1
        if user > pc:
            print("PC number is lower than yours. Choose another number: ")
        else:
            print("PC number is higher than yours. Choose another number: ")
        user = get_user_guess()
    return attempts

def get_user_choice():
    """
    Get the user's choice to play the game again or not.

    Returns:
        bool: True if the user chooses to play again, False otherwise.
    """
    answer = input("").lower()
    while answer not in ['yes', 'y', 'no', 'n']:
        answer = input("Invalid input. Please type yes or no: ").lower()
    if answer == 'yes' or answer == 'y':
        print("Alright! Let's play.")
        return True
    return False

# Main Game Loop
print("Welcome to Guessing the Number Game")
scores = []

print("Would you like to play? (yes/no): ", end="")
choice = get_user_choice()

while choice:
    pc_number = random.randint(1, 10)
    print("\nPC has chosen a number from 1 to 10.")
    user_number = get_user_guess()

    attempts = compare_numbers(user_number, pc_number)
    print(f"Excellent! PC also chose {pc_number}. You got it right in {attempts} attempts.")
    scores.append(attempts)

    print("Would you like to play again? (yes/no): ", end="")
    choice = get_user_choice()

# Display Summary
if scores:
    print("\nHere is a summary of your attempts:")
    for i, s in enumerate(scores, start=1):
        print(f"Game {i}: You guessed the number correctly after {s} attempts.")

print("Have a good day!\n")
