"""
Rock, Paper, Scissors Game
This script implements a simple Rock, Paper, Scissors game where the user competes against the computer.
The user inputs their choice, and the computer generates a random choice. 
The winner is determined, and the result is displayed in a stylized format.

Author: Mahmoud Khalil
Date: 06-12-2023
"""


import random

def user_choice():
    """
    Function to get user input for Rock, Paper, Scissors game.

    Returns:
    str: User's choice ('r', 'p', 's', or 'e' to exit).
    """
    print("Type 'r' for rock, 'p' for paper, or 's' for scissor")
    return input("Otherwise type 'e' to exit: ")

# Main game loop
print("Welcome to Rock, Paper, Scissors game")
while True:
    # Get user's choice
    user = user_choice()

    # Check for exit condition
    if user == 'e':
        break

    # Validate user input
    if user not in ['r', 'p', 's']:
        print("Your input is invalid! ", end="")
        continue

    # Generate computer's choice
    pc = random.choice(['r', 'p', 's'])

    # Determine the winner and print the result
    if user == pc:
        print(f"####      It's a tie! PC also chose {pc}    ####\n")
    elif (user == 'p' and pc == 'r') or (user == 'r' and pc == 's') or (user == 's' and pc == 'p'):
        print(f"####      You won! PC chose {pc}            ####\n")
    else:
        print(f"####      You lost. PC chose {pc}           ####\n")
