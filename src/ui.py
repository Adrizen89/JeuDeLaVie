import tkinter as tk
from game_of_life import next_board_state

class GameOfLifeUI:
    def __init__(self, master, rows=20, cols=20, cell_size=20):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.cells = [[False for _ in range(cols)] for _ in range(rows)]
        self.master.title("Jeu de la Vie")

        self.canvas = tk.Canvas(master, width=self.cols*cell_size, height=self.rows*cell_size)
        self.canvas.pack()

        self.setup_grid()
        self.canvas.bind("<Button-1>", self.toggle_cell)

        start_button = tk.Button(master, text="Démarrer", command=self.start_game)
        start_button.pack()

    def setup_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")

    def toggle_cell(self, event):
        x, y = event.x // self.cell_size, event.y // self.cell_size
        self.cells[y][x] = not self.cells[y][x]
        color = "black" if self.cells[y][x] else "white"
        self.canvas.create_rectangle(x*self.cell_size, y*self.cell_size, (x+1)*self.cell_size, (y+1)*self.cell_size, fill=color)

    def start_game(self):
        self.update_board()
        self.master.after(100, self.start_game)

    def update_board(self):
        self.cells = next_board_state(self.cells)
        for row in range(self.rows):
            for col in range(self.cols):
                color = "black" if self.cells[row][col] else "white"
                self.canvas.create_rectangle(col*self.cell_size, row*self.cell_size, (col+1)*self.cell_size, (row+1)*self.cell_size, fill=color)

if __name__ == "__main__":
    root = tk.Tk()
    gui = GameOfLifeUI(root)
    root.mainloop()
