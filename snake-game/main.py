from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard
from message import Message

STEP_DELAY = 100        # ms mezi kroky hada
GAME_OVER_DELAY = 3000  # ms, jak dlouho je videt GAME OVER

screen = Screen()
screen.bgcolor("green")
screen.title("Vitejte v hadi hre")
screen.setup(width=600, height=600)
screen.tracer(False)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
message = Message()
message.show_intro()

# Kliknuti na klavesy
screen.listen()
screen.onkeypress(snake.up, "w")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.right, "d")
screen.onkeypress(screen.bye, "Escape")


def game_step():
    # Po prvnim stisku klavesy uvodni text zmizi
    if snake.moving and message.visible:
        message.hide()

    snake.move()

    # Kolize s hranou obrazovky nebo s vlastnim telem
    # (musi byt pred jedenim, novy clanek se totiz objevi primo pod hlavou)
    if snake.hit_wall() or snake.hit_tail():
        game_over()
        return

    # Kolize hlavy s jablkem - had sni jablko
    if snake.head.distance(food) < 15:
        snake.grow()
        food.refresh(snake.occupied())
        scoreboard.increase()

    screen.update()
    screen.ontimer(game_step, STEP_DELAY)


def game_over():
    message.show_game_over(scoreboard.score, scoreboard.new_record)
    screen.update()
    # Hra se na chvili zastavi, ale okno dal reaguje (napr. na Escape)
    screen.ontimer(restart, GAME_OVER_DELAY)


def restart():
    snake.reset()
    scoreboard.reset()
    message.show_intro()
    screen.update()
    screen.ontimer(game_step, STEP_DELAY)


screen.update()
screen.ontimer(game_step, STEP_DELAY)
screen.mainloop()
