from turtle import Turtle
FONT = ('Courier', 24, 'normal')
FONT_ALIGNMENT = 'center'
FONT_MOVE = False
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}", move=FONT_MOVE, align=FONT_ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=FONT_MOVE, align=FONT_ALIGNMENT, font=FONT)
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=FONT_MOVE, align=FONT_ALIGNMENT, font=FONT)