import tkinter as tk
import random

# Game of Life class
class GameOfLife:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.canvas_width = width * cell_size
        self.canvas_height = height * cell_size
        self.canvas = None
        self.board = None

    def create_board(self):
        self.board = [[random.choice([0, 1]) for _ in range(self.width)] for _ in range(self.height)]

    def update_board(self):
        new_board = [[0] * self.width for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                count = self.count_neighbors(i, j)
                if self.board[i][j] == 1:
                    if count < 2 or count > 3:
                        new_board[i][j] = 0
                    else:
                        new_board[i][j] = 1
                else:
                    if count == 3:
                        new_board[i][j] = 1
        self.board = new_board

    def count_neighbors(self, row, col):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                neighbor_row = (row + i + self.height) % self.height
                neighbor_col = (col + j + self.width) % self.width
                count += self.board[neighbor_row][neighbor_col]
        return count

    def draw_board(self):
        self.canvas.delete("all")
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 1:
                    x1 = j * self.cell_size
                    y1 = i * self.cell_size
                    x2 = x1 + self.cell_size
                    y2 = y1 + self.cell_size
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")

    def step(self):
        self.update_board()
        self.draw_board()
        self.canvas.after(100, self.step)

    def start(self):
        self.create_board()

        root = tk.Tk()
        root.title("Game of Life")

        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        self.draw_board()

        root.after(100, self.step)
        root.mainloop()


# Create an instance of the GameOfLife class
game = GameOfLife(80, 80, 10)
game.start()
