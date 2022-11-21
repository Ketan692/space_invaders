from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 320)
        self.score = 0

        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High Score : {self.high_score}", align="center", font=("Arial", 18,
                                                                                                     "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
