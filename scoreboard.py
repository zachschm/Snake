from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        # Allows for a high score record across all users
        with open("data.txt", "r") as data:
            self.record = int(data.readline())
        self.update_score()

    # Simply refreshes score to update points total
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}      Record: {self.record}", align="center", font=("Arial", 24, "normal"))

    # Increments the self.score by 1
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    # Gives the user a game over message
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
        if self.score > self.record:
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")









