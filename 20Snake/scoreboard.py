from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = -1
        self.update_score()
        
    def update_score(self):
        self.score += 1
        self.clear()
        self.teleport(0, 230)
        self.write(f"Score: {self.score}", align='center', font=('Comic Sans', 18, 'bold'))
        self.color("white")

    def game_over(self):
        self.teleport(0, 0)
        self.write("Game Over", align='center', font=('Comic Sans', 18, 'bold'))
        