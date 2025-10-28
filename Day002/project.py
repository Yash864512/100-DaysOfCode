print("Welcome to Tip Calculator")
amount = float(input("Enter the total bill: "))
tip = int(input("Enter the tip percentage you wanted to give: "))
num_members = int(input("Enter total number of members: "))

total = (amount + (amount * tip / 100)) / 2
print(f"Each person should pay {total}.")