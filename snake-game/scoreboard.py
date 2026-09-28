from turtle import Turtle
from pathlib import Path
import json

FONT = ("Arial", 18)
# Soubor s nejvyssim skore lezi vedle tohoto skriptu, at uz hru spustite odkudkoli
SAVE_FILE = Path(__file__).parent / "highscore.json"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = self.load_highest_score()
        self.new_record = False
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.update_scoreboard()

    def load_highest_score(self):
        # Kdyz soubor neexistuje nebo je poskozeny, zacneme od nuly
        try:
            with open(SAVE_FILE) as file:
                value = json.load(file)["highest_score"]
        except (OSError, ValueError, KeyError, TypeError):
            return 0
        return value if isinstance(value, int) else 0

    def save_highest_score(self):
        try:
            with open(SAVE_FILE, "w") as file:
                json.dump({"highest_score": self.highest_score}, file)
        except OSError:
            pass  # kdyz se nepodari zapsat, hra ma pokracovat dal

    def update_scoreboard(self):
        self.clear()
        self.write(f"Skore: {self.score} Nejvyssi skore: {self.highest_score}", align="center", font=FONT)

    def increase(self):
        self.score += 10
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.new_record = True
            self.save_highest_score()
        self.update_scoreboard()

    def reset(self):
        self.score = 0
        self.new_record = False
        self.update_scoreboard()
