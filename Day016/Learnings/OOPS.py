import turtle

ram = turtle.Turtle()  # Here ram = object, turtle = package, Turtle() = method
ram.shape("turtle")  # .shape() = method. Usually functions we call from other packages is called methods
ram.color("red")  # .color() is also method
ram.forward(100)  # .forward() is also a method

my_screen = turtle.Screen()  # my_screen = object of screen method, Screen() = method
print(my_screen.canvheight)  # Here canvheight is an attribute which can be called using object
my_screen.exitonclick()  # exitonclick() is also a method

# ----------------------------> Pretty Table package
import prettytable
"""If you want to learn more about pretty table package, visit this website https://pypi.org/project/prettytable/ """
""" https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki """

table = prettytable.PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print("\nThis is from pretty table section.")
print(table)