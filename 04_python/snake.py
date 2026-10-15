import tkinter as tk
import random
import json
import os


WIDTH = 600
HEIGHT = 400
CELL = 20
SPEED = 110

JSON_FILE = "snake_score.json"


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Змейка")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            root,
            width=WIDTH,
            height=HEIGHT,
            bg="black"
        )
        self.canvas.pack()

        self.score_label = tk.Label(
            root,
            text="Счёт: 0",
            font=("Arial", 14)
        )
        self.score_label.pack()

        self.root.bind("<KeyPress>", self.change_direction)

        self.reset()
        self.game_loop()

    # JSON faila ielāde
    def load_score(self):
        if os.path.exists(JSON_FILE):
            try:
                with open(JSON_FILE, "r", encoding="utf-8") as file:
                    data = json.load(file)

                return data.get("apesti_aboli", 0)

            except:
                return 0

        return 0

    # JSON faila saglabāšana
    def save_score(self):
        data = {
            "apesti_aboli": self.total_apples
        }

        with open(JSON_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    # Spēles sākšana / restartēšana
    def reset(self):
        self.snake = [
            (300, 200),
            (280, 200),
            (260, 200)
        ]

        self.direction = "Right"
        self.next_direction = "Right"

        # Šīs spēles rezultāts
        self.score = 0

        # Kopējais apēsto ābolu skaits
        self.total_apples = self.load_score()

        self.game_over = False

        self.food = self.new_food()

        self.score_label.config(
            text=f"Счёт: {self.score}"
        )

        self.draw()

    # Izveido jaunu ābolu
    def new_food(self):
        while True:
            x = random.randrange(0, WIDTH, CELL)
            y = random.randrange(0, HEIGHT, CELL)

            if (x, y) not in self.snake:
                return x, y

    # Tastatūras vadība
    def change_direction(self, event):
        key = event.keysym

        opposite = {
            "Up": "Down",
            "Down": "Up",
            "Left": "Right",
            "Right": "Left"
        }

        # Bultas
        if key in opposite:
            if opposite[key] != self.direction:
                self.next_direction = key

        # Restartēt spēli
        if self.game_over and key == "space":
            self.reset()
            self.game_loop()

        # Izvadīt JSON saglabāto rezultātu
        if key.lower() == "s":
            self.show_saved_score()

    # Izvadīt saglabāto rezultātu
    def show_saved_score(self):
        total = self.load_score()

        self.canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2,
            text=f"Kopā apēsti āboli:\n{total}",
            fill="yellow",
            font=("Arial", 22, "bold")
        )

    # Spēles cikls
    def game_loop(self):
        if self.game_over:
            return

        self.direction = self.next_direction

        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            head_y -= CELL

        elif self.direction == "Down":
            head_y += CELL

        elif self.direction == "Left":
            head_x -= CELL

        elif self.direction == "Right":
            head_x += CELL

        new_head = (head_x, head_y)

        # Sadursme ar sienu
        hit_wall = (
            head_x < 0 or
            head_x >= WIDTH or
            head_y < 0 or
            head_y >= HEIGHT
        )

        # Sadursme ar sevi
        hit_self = new_head in self.snake

        if hit_wall or hit_self:
            self.game_over = True
            self.draw_game_over()
            return

        # Pievienojam jauno galvu
        self.snake.insert(0, new_head)

        # Ja apēsts ābols
        if new_head == self.food:

            # Šīs spēles rezultāts
            self.score += 1

            # Kopējais rezultāts
            self.total_apples += 1

            # Saglabājam JSON failā
            self.save_score()

            self.score_label.config(
                text=f"Счёт: {self.score}"
            )

            # Jauns ābols
            self.food = self.new_food()

        else:
            # Noņemam asti
            self.snake.pop()

        self.draw()

        self.root.after(SPEED, self.game_loop)

    # Zīmē spēli
    def draw(self):
        self.canvas.delete("all")

        # Ābols
        x, y = self.food

        self.canvas.create_oval(
            x + 2,
            y + 2,
            x + CELL - 2,
            y + CELL - 2,
            fill="red",
            outline=""
        )

        # Čūska
        for i, (x, y) in enumerate(self.snake):

            if i == 0:
                color = "lime"
            else:
                color = "green"

            self.canvas.create_rectangle(
                x + 1,
                y + 1,
                x + CELL - 1,
                y + CELL - 1,
                fill=color,
                outline=""
            )

    # Spēles beigas
    def draw_game_over(self):
        self.draw()

        self.canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2 - 40,
            text="ИГРА ОКОНЧЕНА",
            fill="white",
            font=("Arial", 26, "bold")
        )

        self.canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2,
            text=f"Apēsti šajā spēlē: {self.score}",
            fill="yellow",
            font=("Arial", 18)
        )

        self.canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2 + 40,
            text=f"Kopā apēsti: {self.total_apples}",
            fill="yellow",
            font=("Arial", 18)
        )

        self.canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2 + 80,
            text="Space — sākt no jauna    S — parādīt rezultātu",
            fill="white",
            font=("Arial", 14)
        )


root = tk.Tk()

game = SnakeGame(root)

root.mainloop()
