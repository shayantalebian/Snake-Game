import turtle as Turtle_Module

screen = Turtle_Module.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game 🐍 | Shayan Talebian 👨🏻‍💻")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    turtle = Turtle_Module.Turtle(shape="square")
    turtle.color("white")
    turtle.goto(position)

    

screen.exitonclick()