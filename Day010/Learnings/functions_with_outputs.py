def format_name(first_name, last_name):  # Defining a function with parameters
    """Takes first name and last name as parameters
    and returns the Title Case formatted name"""
    # DocString declaration. When you hover your curser on function name it shows the docstring

    if first_name == "" and last_name == "":  # Checking if user provides empty arguments
        return "Please provide inputs"

    formatted_f_name = first_name.title()  # Formatting to Title Case
    formatted_l_name = last_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


print(format_name(input("What is your first name? "), input("What is your last name? ")))

# --------------> Function as an argument for another function


def fun1(text):  # Defining normal function with 'text' as parameter
    return text + " " + text


def fun2(text):  # Defining normal function with 'text' as parameter
    return text.title()


output = fun2(fun1("hEllO"))  # The return value of fun1 is used as argument for fun2
print(output)