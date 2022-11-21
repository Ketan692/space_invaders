import turtle, random
from turtle import Turtle, Screen
from enemy import Enemy
from player import Player
from scoreboard import ScoreBoard

window = Screen()
window.setup(width=600, height=700, startx=450, starty=10)
window.bgcolor("black")
window.title("Space Invaders")


player = Player()
enemy = Enemy()
scoreboard = ScoreBoard()

bullet = Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bullet_speed = 100
bullet_state = "ready"


def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        x = player.players_pos()[0]
        y = player.players_pos()[1] + 10
        bullet.setposition(x, y)
        bullet.showturtle()


turtle.listen()
turtle.onkey(player.move_left, "Left"), turtle.onkey(player.move_right, "Right"), turtle.onkey(fire_bullet, "space")


for i in range(500):
    enemy.move()

    x = bullet.ycor()
    x += bullet_speed
    bullet.sety(x)

    if bullet.ycor() > 340:
        bullet.hideturtle()
        bullet_state = "ready"

    for e in enemy.enemy_list():
        if e.distance(bullet) < 20:
            bullet.hideturtle()
            bullet.penup()
            scoreboard.increase_score()
            bullet.setposition(0, -300)
            bullet_state = "ready"
            e.setposition(random.randint(-250, 250), random.randint(200, 330))

        if e.ycor() < -300:
            scoreboard.reset()
            print("game_over")
            window.bye()
            break
    else:
        continue
    break


window.mainloop()
