# Include an ASCII art logo.
from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")

def guess_number():
    print("I'm thinking of a number between 1 and 100.")
    return random.randrange(100)


random_number = (guess_number())
# Uncomment below for testing purposes
# print(random_number)
number_of_guesses = 10
is_game_over = False

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
def compare(guess):
    if guess > random_number:
        print("Too high.")
        return number_of_guesses - 1
    elif guess < random_number:
        print("Too low.")
        return number_of_guesses - 1


# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
if input("Choose a difficulty. Type 'easy' or 'hard': ") == "hard":
    number_of_guesses = 5

# Track the number of turns remaining.
while number_of_guesses > 0:
    print(f"You have {number_of_guesses} attempts remaining to guess the number.")
    # Allow the player to submit a guess for a number between 1 and 100.
    guess = int(input("Guess the number: "))
    if guess == random_number:
        # If they got the answer correct, show the actual answer to the player.
        print(f"You got it! The answer was {random_number}.")
        is_game_over = True
        number_of_guesses = 0
    else:
        number_of_guesses = compare(guess)

# If they run out of turns, provide feedback to the player.
if is_game_over != True:
    print("You've run out of guesses, you lose.")












