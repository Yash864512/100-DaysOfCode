# The dictionary which is a pair of 'Key': 'Value'
dictionary = {
    "bug": "An error, fault, or flaw in a computer program that causes it to produce an incorrect or unexpected result, or to behave in an unintended way",
    "Function": "A block of organized, reusable code designed to perform a specific task."
}

print(dictionary["bug"])  # Accessing value of a key in dictionary using key
# Adding a new key and value pair into dictionary
dictionary["Object Oriented Programming"] = "A programming paradigm that organizes code around objects, which are software entities that contain both data (attributes) and functions (methods)."
# Changing already existing key value
dictionary["bug"] = "A bug is an insect."
print(dictionary["Object Oriented Programming"])
print(dictionary["bug"])

capitals = {  # Dictionary that represents Countries(France, Germany) as key and cities(Paris, berlin) as values of the respected key
    "France": "Paris",  # key = France, value = Paris
    "Germany": "Berlin"
}

travel_log = {  # Nesting a list in the dictionary as Value of a key
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

print(travel_log["France"][2])  # Accessing 'Dijon'

nested_list = [1, 2, [3, 4]]  # Nested list: List inside a list
print(nested_list[2])

travel_log_detailed = {  # Nesting a dictionary inside a dictionary
    "France": {
        "no_of_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "no_of_times_visited": 10,
        "cities_visited": ["Stuttgart", "Berlin"]
    }
}

print(travel_log_detailed["France"]["cities_visited"][2])  # Accessing 'Dijon'
