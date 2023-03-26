from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")

# Reading high_score from data.txt
with open("data.txt") as data:
    HIGH_SCORE = int(data.read())

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = HIGH_SCORE
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False, ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # Writing new high score to data
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()