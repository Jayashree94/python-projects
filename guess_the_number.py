import random
import logo_art
EASY_LEVEL_ATTEMPTS = 10 
HARD_LEVEL_ATTEMPTS = 5
def set_difficulty(level):
    if level == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif level == "hard":
        return HARD_LEVEL_ATTEMPTS
    else: 
        return 
    
def check_answer(guess, answer, attempts):
    if guess < answer:
        print("Your guess is Too low.")
        return attempts - 1
    elif guess > answer:
        print("Your guess is Too high.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return attempts

def game():
    print(logo_art.logo)
    print("Let me think of a number between 1 and 50")
    answer =random.randint(1,50)
    level = input("Choose a level: easy or hard: ")
    attempts = set_difficulty(level)
    if attempts != EASY_LEVEL_ATTEMPTS and attempts != HARD_LEVEL_ATTEMPTS:
        print("Invalid level. Please choose 'easy' or 'hard'. Play again")
        return
        


    guess = 0
    while(guess != answer):
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Guess a number between 1 and 50: "))
        attempts =check_answer(guess, answer, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
game()
