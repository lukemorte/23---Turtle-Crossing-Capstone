from turtle import Turtle


FONT = ("Courier", 18, "bold")
FONT_GAME_OVER = ("Courier", 30, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.lives = 3

        self.render()

    def render(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-270, 250)
        self.write(f"Level: {self.level}", False, align="left", font=FONT)
        self.goto(250, 250)
        self.write(f"Lives: {self.lives}", False, align="right", font=FONT)

    def level_increment(self):
        self.level += 1
        self.render()

    def lives_decrement(self):
        self.lives -= 1
        self.render()

    def render_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=FONT_GAME_OVER)
