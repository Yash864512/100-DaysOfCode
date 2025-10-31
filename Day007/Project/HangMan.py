import random
import ASCII
import Words
print(ASCII.title)

random_choice = random.choice(Words.word_list)  # Gives random word

# Displaying number of '_' for number of letters in word
placeholder = ""
for letter in range(len(random_choice)):
    placeholder += "_"
print(placeholder)

correct_letters = []
game_over = False
chances = 6  # Number of Chances
# Game loop
while not game_over:
    user_guess = input("\nGuess the letter in the word: ").lower()
    display = ""
    for letter in random_choice:  # Checking if user_guess is there in word
        if letter == user_guess:
            display += user_guess
            print(ASCII.stages[chances])
            if user_guess not in correct_letters:
                correct_letters.append(user_guess)  # Appending matched letters in correct_letters list
        elif letter in correct_letters:  # Maintaining the consistency of found letters
            display += letter
        else:
            display += "_"  # Displaying _ if the letter is not present in that place
    print(display)

    if user_guess not in random_choice:  # Conditions if the user_guess is not there in word
        chances -= 1
        print(ASCII.stages[chances])
        print(f"\n'{user_guess}' is not there in the chosen word.")
        print(f"***********You have {chances} chances left.***********")

    # Checking if game should continue or not
    if "_" not in display:  # First condition to stop the game
        game_over = True
        print("The word is " + random_choice)
        print("******************YOU WIN!******************")
    elif chances == 0:  # Second condition to stop the game
        game_over = True
        print("The word is " + random_choice)
        print("******************YOU LOST!******************")
