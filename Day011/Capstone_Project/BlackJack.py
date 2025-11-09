import random
import logo


def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Values of cards
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Calculates the scores of the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # '0' in our code means the user/computer has won

    if sum(cards) > 21 and 11 in cards:  # If sun of cards is > 21 and ACE(11) is present in the cards, we can change 11 to 1.
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_scr, computer_scr):
    """Compares user's score and computer's score and returns the message"""
    if computer_scr == user_scr:
        return "It's a Draw!"
    elif computer_scr == 0:
        return "Lose, Opponent has a BlackJack."
    elif user_scr == 0:
        return "Win with a BlackJack."
    elif computer_scr > 21:
        return "Opponent went over, You win."
    elif user_scr > 21:
        return "You went over, You lose."
    elif user_scr > computer_scr:
        return "You Win."
    else:
        return "You Lose."


def play_game():
    print(logo.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1  # Here we chose -1 instead of 0 because 0 represents won in our game
    user_score = -1
    is_game_over = False
    for _ in range(2):  # Drawing 2 random cards each for user and computer
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:  # Condition for win
            is_game_over = True
        else:  # Condition if user wants to get another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:  # Drawing random cards for computer
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play the game of BlackJack('y' for yes and 'n' for no): ").lower() == 'y':
    print("\n" * 100)
    play_game()
