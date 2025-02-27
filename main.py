import turtle as Turtle_Module
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time as Time

screen = Turtle_Module.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game 🐍 | Shayan Talebian 👨🏻‍💻")
screen.tracer(0)    

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="d", fun=snake.right)
    
game_is_on = True
while game_is_on:
    screen.update()
    Time.sleep(0.1)
    
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        
    
screen.exitonclick()
