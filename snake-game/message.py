from turtle import Turtle

FONT = "Arial"


class Message(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.visible = False

    def write_line(self, text, y, size, style="normal", color="white"):
        self.color(color)
        self.goto(0, y)
        self.write(text, align="center", font=(FONT, size, style))

    def show_intro(self):
        # Text je ve spodni polovine, aby nezakryval hada a jablko
        self.clear()
        self.write_line("VITEJTE V HADI HRE", -70, 26, "bold")
        self.write_line("Ovladani:", -115, 16, "bold", "gold")
        self.write_line("W  -  nahoru", -145, 14)
        self.write_line("S  -  dolu", -167, 14)
        self.write_line("A  -  doleva", -189, 14)
        self.write_line("D  -  doprava", -211, 14)
        self.write_line("Pro start stisknete kteroukoli z klaves W A S D", -255, 14, "italic", "gold")
        self.visible = True

    def show_game_over(self, score, new_record):
        self.clear()
        self.write_line("GAME OVER", 40, 40, "bold", "red")
        self.write_line(f"Vase skore: {score}", -10, 22)
        if new_record:
            self.write_line("Blahopreji, udelal jste novy rekord!", -50, 16, "bold", "gold")
        self.visible = True

    def hide(self):
        self.clear()
        self.visible = False
