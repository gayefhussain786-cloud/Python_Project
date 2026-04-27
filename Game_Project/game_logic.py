# game_logic.py
import random

def get_computer_choice():
    return random.choice(['Stone', 'Paper', 'Scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    
    # Winning conditions for the user
    win_conditions = {
        'Stone': 'Scissors',
        'Paper': 'Stone',
        'Scissors': 'Paper'
    }
    
    if win_conditions[user] == computer:
        return "You Win!"
    else:
        return "Computer Wins!"