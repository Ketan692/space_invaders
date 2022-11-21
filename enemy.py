from turtle import Turtle
import random

ENEMY_SPEED = 2


class Enemy:

    def __init__(self):
        self.positions = []
        self.create_enemy()

    def create_enemy(self):
        for i in range(5):
            enemy = Turtle()
            enemy.color("white")
            enemy.penup()
            enemy.speed(0)
            enemy.shape("circle")
            enemy.goto(random.randint(-250, 250), random.randint(200, 280))
            self.positions.append(enemy)

    def move(self):
        global ENEMY_SPEED
        for i in self.positions:
            if i.xcor() > 260:
                for k in self.positions:
                    k.sety(k.ycor() - 40)
                ENEMY_SPEED *= -1
            elif i.xcor() < -260:
                for k in self.positions:
                    k.sety(k.ycor() - 40)
                ENEMY_SPEED *= -1
            enemy_x = i.xcor() + ENEMY_SPEED
            i.setx(enemy_x)

    def enemy_list(self):
        return self.positions






