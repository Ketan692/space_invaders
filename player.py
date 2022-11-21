from turtle import Turtle
MOVING_SPEED = 15

class Player:

    def __init__(self):
        self.name = Turtle()
        self.name.setheading(90)
        self.name.penup()
        self.name.speed(0)
        self.name.shape("triangle")
        self.name.goto(0, -330)
        self.name.color("white")

    def move_left(self):
        x = self.name.xcor()
        if x > -250:
            x -= MOVING_SPEED
            self.name.setx(x)

    def move_right(self):
        x = self.name.xcor()
        if x < 250:
            x += MOVING_SPEED
            self.name.setx(x)

    def players_pos(self):
        pos = self.name.xcor()
        pos2 = self.name.ycor()
        return [pos, pos2]

    def plr(self):
        return self.name





