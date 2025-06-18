#!/bin/python3
# MasterMind
# by ICTROCN (aangepast door jou)
# v1.02
# 18-6-2025
# Verwijderd backdoor, invoer met cijfers 1-6, replay-loop toegevoegd

import random

def generate_code(length=4, digits=6):
    return [str(random.randint(1, digits)) for _ in range(length)]

def get_feedback(secret, guess):
    black_pegs = sum(s == g for s, g in zip(secret, guess))
    
    secret_counts = {}
    guess_counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_counts[s] = secret_counts.get(s, 0) + 1
            guess_counts[g] = guess_counts.get(g, 0) + 1

    white_pegs = sum(min(secret_counts.get(d, 0), guess_counts.get(d, 0)) for d in guess_counts)
    
    return black_pegs, white_pegs

def play_mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4-digit code. Each digit is from 1 to 6. You have 10 attempts.")
    
    secret_code = generate_code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        valid_guess = False
        while not valid_guess:
            guess = input(f"Attempt {attempt}: ").strip()
            if len(guess) == 4 and all(c in "123456" for c in guess):
                valid_guess = True
            else:
                print("Invalid input. Enter exactly 4 digits, each between 1 and 6.")
        
        black, white = get_feedback(secret_code, guess)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: {''.join(secret_code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {''.join(secret_code)}")

if __name__ == "__main__":
    play_again = 'Y'
    while play_again == 'Y':
        play_mastermind()
        play_again = input("Play again? (Y/N): ").upper()
        while play_again not in ['Y', 'N']:
            play_again = input("Please enter Y or N: ").upper()

