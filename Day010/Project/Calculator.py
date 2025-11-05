"""def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

final_value = 0
should_continue = True
num1 = 0
while should_continue:
    if final_value == 0:
        num1 = float(input("Type the 1st number: "))
        operator = input("Type the operator: ")
        num2 = float(input("Type the 2nd number: "))
        final_value = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {final_value}")
        choice = input(f"Do you want to do another mathematical operation with {final_value}. Type 'yes' or 'no': ").lower()
        if choice == "yes":
            num1 = final_value
        else:
            should_continue = False
    else:
        operator = input("Type the operator: ")
        num2 = float(input("Type the 2nd number: "))
        final_value = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {final_value}")
        choice = input(
            f"Do you want to do another mathematical operation with {final_value}. Type 'yes' or 'no'").lower()
        if choice == "yes":
            num1 = final_value
        else:
            should_continue = False
"""

# -----------------------> More compact version of calculator
"""As previous version of code has repeated lines of code here is the compact version of
calculator"""
import logo
print(logo.logo)


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print("Welcome to the Python Calculator")

    while True:
        num1 = float(input("What's the first number?: "))

        while True:
            for symbol in operations:
                print(symbol)

            operation_symbol = input("Pick an operation: ")
            num2 = float(input("What's the next number?: "))

            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")

            choice = input(f"Type 'y' to continue with {answer}, 'n' for a new calculation, or 'e' to exit: ").lower()

            if choice == 'y':
                num1 = answer
            elif choice == 'n':
                print("\n" * 5)
                break
            elif choice == 'e':
                print("Exiting calculator. Goodbye!")
                return
            else:
                print("Invalid input. Exiting.")
                return


calculator()
