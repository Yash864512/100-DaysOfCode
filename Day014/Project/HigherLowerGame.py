import random
import Personalities
import logo

print(logo.logo)
score = 0
is_game_over = False


def celebs():
    celeb = random.choice(Personalities.persons)
    return celeb


compare = celebs()
while not is_game_over:
    against = celebs()
    while against == compare:
        against = celebs()

    print(f"Compare A: {compare["name"]}, {compare["description"]}, from {compare["country"]}")
    print(logo.vs)
    print(f"Against B: {against["name"]}, {against["description"]}, from {against["country"]}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if user_choice == "A" and compare["follower_count"] > against["follower_count"]:
        score += 1
        print("\n" * 100)
        print(f"You're right! Current score: {score}")
    elif user_choice == "A" and compare["follower_count"] < against["follower_count"]:
        print()
        print(f"Sorry, that's wrong. Final score: {score}")
        is_game_over = True
    elif user_choice == "B" and compare["follower_count"] < against["follower_count"]:
        score += 1
        print("\n" * 100)
        compare = against
        print(f"You're right! Current score: {score}")
    elif user_choice == "B" and compare["follower_count"] > against["follower_count"]:
        print()
        print(f"Sorry, that's wrong. Final score: {score}")
        is_game_over = True
    else:
        print(f"Invalid Input. Final score: {score}")
        is_game_over = True
