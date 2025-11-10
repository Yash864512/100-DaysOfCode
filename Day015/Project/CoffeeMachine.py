WATER = 500
COFFEE = 100
MILK = 300
MONEY = 0

FIVES = 0
TENS = 0
HUNDREDS = 0


def availability(coffee_type, inserted_money):
    global turn_off, MONEY, WATER, COFFEE, MILK
    if coffee_type == "espresso":
        if WATER >= 50 and COFFEE >= 18:
            if inserted_money >= 110:
                print("Here is your espresso! Enjoy it.")
                WATER -= 50
                COFFEE -= 18
                change = inserted_money - 110
                MONEY += 110
                print(f"Here is your change of: {change}")
            else:
                print("Not enough Money. Here is your money back")
            return True
        else:
            print("Sorry! There are not enough resources left in the machine.")
    elif coffee_type == "latte":
        if WATER >= 200 and COFFEE >= 24 and MILK >= 150:
            if inserted_money >= 210:
                print("Here is your latte! Enjoy it.")
                WATER -= 200
                COFFEE -= 24
                MILK -= 150
                change = inserted_money - 210
                MONEY += 210
                print(f"Here is your change of: {change}")
            else:
                print("Not enough Money. Here is your money back")
            return True
        else:
            print("Sorry! There are not enough resources left in the machine.")
    elif coffee_type == "cappuccino":
        if WATER >= 250 and COFFEE >= 24 and MILK >= 100:
            if inserted_money >= 250:
                print("Here is your cappuccino! Enjoy it.")
                WATER -= 250
                COFFEE -= 24
                MILK -= 100
                change = inserted_money - 250
                MONEY += 250
                print(f"Here is your change of: {change}")
            else:
                print("Not enough Money. Here is your money back")
            return True
        else:
            print("Sorry! There are not enough resources left in the machine.")
    elif coffee_type == "report":
        print(f"<-----Resources left----->\nWater: {WATER}\nCoffee: {COFFEE}\nMilk: {MILK}\nMoney: {MONEY}\n")
    elif coffee_type == "off":
        turn_off = True
    else:
        print("Incorrect choice")


turn_off = False

while not turn_off:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice in ["espresso", "latte", "cappuccino"]:
        print("Please insert coins.")
        FIVES = int(input("How many fives: "))
        TENS = int(input("How many tens: "))
        HUNDREDS = int(input("How many hundreds: "))
        inserted_money = HUNDREDS * 100 + TENS * 10 + FIVES * 5
        availability(choice, inserted_money)
    elif choice == "report":
        availability(choice, 0)
    elif choice == "off":
        availability(choice, 0)
    else:
        print("Invalid input. Please choose again.")
