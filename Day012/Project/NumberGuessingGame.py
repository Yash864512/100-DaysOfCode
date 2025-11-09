import random
import logo

EASY = 10
HARD = 5

print(logo.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")
number = random.randint(1, 101)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

is_game_over = False
attempts_left = 0

if difficulty == 'easy':
    attempts_left = EASY
    print(f"You have {attempts_left} attempts left.")
elif difficulty == 'hard':
    attempts_left = HARD
    print(f"You have {attempts_left} attempts left.")
else:
    attempts_left = EASY
    print(f"Invalid choice! Defaulting to easy mode. You have {attempts_left} attempts left.")

while not is_game_over:
    print()
    guess = int(input("Make a guess: "))
    if guess < number:
        attempts_left -= 1
        print("Too Low")
    elif guess > number:
        attempts_left -= 1
        print("Too High")
    elif guess == number:
        print(f"You won! The number is {number}.")
        is_game_over = True
    if not is_game_over:
        print(f"You have {attempts_left} attempts left.")
    if attempts_left == 0:
        print("You lost! You are out of attempts.")
        is_game_over = True
