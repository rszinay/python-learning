from turtle import Turtle

STEP = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0
WALL = 290


class Snake:
    def __init__(self):
        self.segments = []
        self.moving = False
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Had zacina jen s hlavou, ta je cerna
        self.add_segment((0, 0), "black")

    def add_segment(self, position, color="grey"):
        segment = Turtle("square")
        segment.color(color)
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def grow(self):
        # Novy clanek se objevi tam, kde je konec ocasu
        self.add_segment(self.segments[-1].position())

    def move(self):
        if not self.moving:
            return

        # Kazdy clanek se presune na misto toho pred nim (od konce k hlave)
        for index in range(len(self.segments) - 1, 0, -1):
            self.segments[index].goto(self.segments[index - 1].position())

        self.head.forward(STEP)

    def turn(self, direction, opposite):
        # Zakaz otoceni o 180 stupnu, dokud had jede
        if self.moving and self.head.heading() == opposite:
            return
        self.head.setheading(direction)
        self.moving = True

    def up(self):
        self.turn(UP, DOWN)

    def down(self):
        self.turn(DOWN, UP)

    def left(self):
        self.turn(LEFT, RIGHT)

    def right(self):
        self.turn(RIGHT, LEFT)

    def hit_wall(self):
        return abs(self.head.xcor()) > WALL or abs(self.head.ycor()) > WALL

    def hit_tail(self):
        for segment in self.segments[1:]:
            if segment.distance(self.head) < STEP / 2:
                return True
        return False

    def occupied(self):
        return [segment.position() for segment in self.segments]

    def reset(self):
        # Skryjeme stare clanky a zacneme znovu jen s hlavou
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.moving = False
        self.create_snake()
        self.head = self.segments[0]
