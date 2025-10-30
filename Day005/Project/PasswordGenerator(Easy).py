import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '~']

print("Welcome to Password Generator\n")
no_of_letters = int(input("How many letters you want to have in your password: "))
no_of_numbers = int(input("How many numbers you want to have in your password: "))
no_of_symbols = int(input("How many symbols you want to have in your password: "))

password = ""
for letter in range(no_of_letters):
    password += random.choice(letters)   # Retrieving random letter from list
for number in range(no_of_numbers):
    password += random.choice(numbers)   # Retrieving random number from list
for symbol in range(no_of_symbols):
    password += random.choice(symbols)   # Retrieving random symbol from list

print(password)
