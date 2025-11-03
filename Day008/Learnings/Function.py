def greet():  # Defining function with zero parameters
    print("Hello!")
    print("How are you?")
    print("How is the weather in your location?\n")


# Calling the function. Output is based on function
greet()


def greet_with_name(name, location):  # Defining function with two parameters
    print(f"Hello! {name}")
    print("How are you?")
    print(f"How is the weather in your {location}?\n")


# Calling function with two arguments
greet_with_name("Yaswanth", "Punjab")


def greet_with_name(name, location):  # Defining function with two parameters
    print(f"Hello! {name}")
    print("How are you?")
    print(f"How is the weather in your {location}?\n")


# Calling function with two arguments specifying the parameters
greet_with_name(location="Punjab", name="Yaswanth")

