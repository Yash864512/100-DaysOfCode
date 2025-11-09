"""Day13 is basically about how to handle bugs and how to use debugger."""

try:
    age = int(input("Type your age: "))
except ValueError:
    print("Invalid. Age should be in number. Try typing a number like 15.")
    age = int(input("Type your age: "))

if age >= 18:
    print(f"At your age({age}) you can drive")
else:
    print("You are under age. You shouldn't drive.")