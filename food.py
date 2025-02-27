import random as Random_Module
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh([])  # Start with an empty list to avoid errors
        
    def refresh(self, snake_segments):
        while True:
            random_x = Random_Module.randint(-280, 280)
            random_y = Random_Module.randint(-280, 280)
            new_position = (random_x, random_y)

            # Ensure food does not spawn on the snake
            if all(segment.distance(new_position) > 15 for segment in snake_segments):
                self.goto(random_x, random_y)
                break
