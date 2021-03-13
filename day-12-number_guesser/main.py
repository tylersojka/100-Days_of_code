import random

def random_number():
    mystery_number = random.randint(1, 100)
    return mystery_number

def difficulty():
    guesses = 0
    level = input("what level of difficulty would you like, type 'Hard', 'Medium', 'Easy'.\n").lower()
    if level = "hard":
        guesses = 5
        return guesses
    elif level = "medium":
        guesses = 7
        return guesses
    elif level = "easy":
        guesses = 10
        return guesses

def compare_number(mystery_number, guess):
    if mystery_number > guess:
        print("your guess is too low")
    elif mystery_number < guess:
        print("your number is too high")
    elif mystery_number == guess:
        print("you win")
        

def welcome():
    print("welcome to the number guessing game")
