enemies = 1


def increase_enemies():
    global enemies  # Can change global variable from a function that effects the original value which cannot be done if global is not declared
    enemies += 1
    print(f"Enemies inside function: {enemies}")


increase_enemies()
print(f"Enemies outside function: {enemies}")


PI = 3.14  # If there is a constant value, assign it a name which is all upper case(Indicates constant when you try to change the value in a function)
GOOGLE_URL = "www.google.com"
