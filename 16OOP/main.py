# from turtle import Turtle, Screen

# tarta = Turtle()

# tarta.shape('turtle')
# tarta.color('blue')
# tarta.forward(100)
# Screen().exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['xubangas', "xubingas", "choupanas"]
table.add_row(["cuba", "cubo", "quibas"])
table.add_row(["youre", "mód", "dder"])
table.add_row(["out", "tari", "or"])
table.add_column("XUPARED", ["xu","ban","gas"])
table.align = "l"
print(table)