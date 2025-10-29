import random

computer_choice = random.randint(0, 2)
player_choice = int(input("Enter your choice(0 for rock, 1 paper and 2 for Scissors): "))
while player_choice > 2 or player_choice < 0:
    print("Please enter valid number")
    player_choice = int(input("Enter your choice(0 for rock, 1 paper and 2 for Scissors): "))

if computer_choice == 0 and player_choice == 1:
    print("Computer chose Rock and you chose Paper. So, ")
    print("You won!")  # Rock and Paper
elif computer_choice == 0 and player_choice == 2:
    print("Computer chose Rock and you chose Scissors. So, ")
    print("You lost!")  # Rock and Scissors
elif computer_choice == 1 and player_choice == 0:
    print("Computer chose Paper and you chose Rock. So, ")
    print("You Lost!")  # Paper and Rock
elif computer_choice == 1 and player_choice == 2:
    print("Computer chose Paper and you chose Scissors. So, ")
    print("You won!")  # Paper and Scissors
elif computer_choice == 2 and player_choice == 0:
    print("Computer chose Scissors and you chose Rock. So, ")
    print("You won!")  # Scissors and Rock
elif computer_choice == player_choice:
    print("It's a draw.")
else:
    print("Computer chose Scissors and you chose paper. So, ")
    print("You lost")  # Scissors and paper

#  -------------------> Optimized Code

'''import random

hands = [
    "✊ Rock",
    "✋ Paper",
    "✌️ Scissors"
]

outcomes = {
    (0, 2): "You win!",
    (1, 0): "You win!",
    (2, 1): "You win!",
    (0, 1): "You lose!",
    (1, 2): "You lose!",
    (2, 0): "You lose!"
}

player = int(input("Enter your choice (0: Rock, 1: Paper, 2: Scissors): "))
while player not in [0, 1, 2]:
    player = int(input("Invalid! Enter 0 for Rock, 1 for Paper, or 2 for Scissors: "))

computer = random.randint(0, 2)

print(f"\nYou chose {hands[player]}")
print(f"Computer chose {hands[computer]}\n")

if player == computer:
    print("It's a draw!")
else:
    print(outcomes.get((player, computer)))
'''
