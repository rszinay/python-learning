English | [Čeština](README.cs.md)

# Snake game (version 2)

The classic snake game written in Python with the `turtle` library. Version 2 is rewritten into objects (classes `Snake`, `Food`, `Scoreboard`, `Message`).

You steer the snake, collect red apples and try not to hit the edge of the window or your own body. Each apple gives 10 points and makes the snake longer. When you crash, the game shows your score (and congratulates you on a new record) and starts again.

The texts shown in the game window are in Czech.

## Requirements

- Python 3.8 or newer
- the `turtle` library (part of Python; it needs `tkinter`)

Nothing to install, no extra packages are needed.

To check that everything works:

```bash
python3 -c "import tkinter; print('OK')"
```

If it prints an error and you use Python from Homebrew, install it with `brew install python-tk`.

## Running

From the `snake-game` folder:

```bash
python3 main.py
```

## Controls

| Key | Action |
|-----|--------|
| **W** | up |
| **S** | down |
| **A** | left |
| **D** | right |
| **Esc** | quit the game (closes the window) |

The game starts when you press any of W, A, S, D. The snake cannot turn 180° (for example, from moving right straight to left). You can also quit by closing the window.

## High score

The high score is saved to `highscore.json`, which is created next to the scripts when the first record is set. It is loaded on the next start and the game continues from it. To start from zero again, delete the file.

## Project structure

| File | Contents |
|------|----------|
| `main.py` | game window, controls and the game loop (`ontimer` + `mainloop`) |
| `snake.py` | class `Snake` – body, movement, growth, collisions |
| `food.py` | class `Food` – the apple, placed at a random spot away from the snake |
| `scoreboard.py` | class `Scoreboard` – score, high score, record, loading and saving to a file |
| `message.py` | class `Message` – intro screen and the GAME OVER message |
| `highscore.json` | saved high score (created automatically with the first record) |

## Ideas for improvement

- Save the player's **name** with the high score. After a record, ask for a name (`screen.textinput`), store it in `highscore.json` next to the score and show it in the score line at the top.
- Steering with the arrow keys.
- Speeding the snake up as the score grows.
