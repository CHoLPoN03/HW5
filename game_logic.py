import random

def play_round(bet, chosen_number):
    winning_number = random.randint(1, 10)
    if chosen_number == winning_number:
        return bet * 2, winning_number
    else:
        return -bet, winning_number
