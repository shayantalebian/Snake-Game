import turtle as Turtle_Module
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = RIGHT
                
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    def add_segment(self, position):
        new_segment = Turtle_Module.Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)   
            
    def extend(self):
        self.add_segment(self.segments[-1].position())
            
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.direction != DOWN:
            self.head.setheading(UP)
            self.direction = UP
    
    def down(self):
        if self.direction != UP:
            self.head.setheading(DOWN)
            self.direction = DOWN

    def left(self):
        if self.direction != RIGHT:  
            self.head.setheading(LEFT)
            self.direction = LEFT

    def right(self):
        if self.direction != LEFT: 
            self.head.setheading(RIGHT)
            self.direction = RIGHT
