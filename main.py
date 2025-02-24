import turtle as Turtle_Module
from snake import Snake
import time as Time

screen = Turtle_Module.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game 🐍 | Shayan Talebian 👨🏻‍💻")
screen.tracer(0)

snake = Snake()
    
game_is_on = True
while game_is_on:
    screen.update()
    Time.sleep(0.1)
    snake .move()
    
screen.exitonclick()
