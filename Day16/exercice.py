import turtle
from prettytable import PrettyTable

# t = turtle.Turtle()
# t.shape("turtle")
# t.color("red", "DarkGoldenrod1")
# t.forward(100)

# screen = turtle.Screen()
# screen.exitonclick()

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu"])
table.add_column("Type", ["Electric"])

table.align = "c"

print(table)