from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("red")
        self.penup()
        self.goto(100, 100)

    def refresh(self, forbidden=()):
        # Jablko se objevi na mrizce po 20 px a nikdy ne na hadovi
        while True:
            x = random.randrange(-280, 281, 20)
            y = random.randrange(-280, 281, 20)
            if (x, y) not in [(round(px), round(py)) for px, py in forbidden]:
                break
        self.goto(x, y)
