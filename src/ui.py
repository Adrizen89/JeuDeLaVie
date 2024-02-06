import tkinter as tk
from tkinter import messagebox
from auth import verify_user, create_user
from game_of_life import next_board_state

class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title("Connexion - Jeu de la Vie")

        self.label_username = tk.Label(master, text="Nom d'utilisateur")
        self.label_username.pack()

        self.entry_username = tk.Entry(master)
        self.entry_username.pack()

        self.label_password = tk.Label(master, text="Mot de passe")
        self.label_password.pack()

        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack()

        self.button_login = tk.Button(master, text="Connexion", command=self.login)
        self.button_login.pack()
        
        self.button_register = tk.Button(master, text="S'inscrire", command=self.open_registration_window)
        self.button_register.pack()
        
    def open_registration_window(self):
        self.registration_window = tk.Toplevel(self.master)
        self.registration_window.title("Inscription")

        self.label_new_username = tk.Label(self.registration_window, text="Nom d'utilisateur")
        self.label_new_username.pack()

        self.entry_new_username = tk.Entry(self.registration_window)
        self.entry_new_username.pack()

        self.label_new_password = tk.Label(self.registration_window, text="Mot de passe")
        self.label_new_password.pack()

        self.entry_new_password = tk.Entry(self.registration_window, show="*")
        self.entry_new_password.pack()

        self.button_create_account = tk.Button(self.registration_window, text="Créer le compte", command=self.register_new_user)
        self.button_create_account.pack()
    
    def register_new_user(self):
        new_username = self.entry_new_username.get()
        new_password = self.entry_new_password.get()

        if new_username and new_password:
            create_user(new_username, new_password)
            messagebox.showinfo("Succès", "Compte créé avec succès")
            self.registration_window.destroy()
        else:
            messagebox.showerror("Erreur", "Le nom d'utilisateur et le mot de passe sont requis")

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if verify_user(username, password):
            messagebox.showinfo("Succès", "Connexion réussie")
            self.master.destroy()
            main_game_window()
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")

class GameOfLifeUI:
    def __init__(self, master, rows=20, cols=20, cell_size=20):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.cells = [[False for _ in range(cols)] for _ in range(rows)]
        master.title("Jeu de la Vie")

        self.canvas = tk.Canvas(master, width=self.cols*self.cell_size, height=self.rows*self.cell_size)
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

def main_login_window():
    root = tk.Tk()
    login_window = LoginWindow(root)
    root.mainloop()

def main_game_window():
    root = tk.Tk()
    game_window = GameOfLifeUI(root)
    root.mainloop()

if __name__ == "__main__":
    main_login_window()
