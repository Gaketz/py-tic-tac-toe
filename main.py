import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.computer_turn = False

        self.loading_label = tk.Label(root, text="Loading...")
        self.loading_label.grid(row=3, columnspan=3)
        self.root.after(1000, self.remove_loading)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_board)
        self.reset_button.grid(row=4, columnspan=3)

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    root,
                    text="",
                    font=("Helvetica", 20),
                    width=5,
                    height=2,
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j)

    def remove_loading(self):
        self.loading_label.grid_remove()

    def make_move(self, row, col):
        if self.board[row][col] == "" and not self.check_winner() and not self.computer_turn:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif all(self.board[i][j] != "" for i in range(3) for j in range(3)):
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_board()
            else:
                self.computer_turn = True
                self.make_computer_move()  # Move this line to avoid changing player here

    def make_computer_move(self):
        if not self.check_winner() and not all(self.board[i][j] != "" for i in range(3) for j in range(3)):
            empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ""]
            row, col = random.choice(empty_cells)
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O")
            self.computer_turn = False
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", "Computer wins!")
                self.reset_board()
            elif all(self.board[i][j] != "" for i in range(3) for j in range(3)):
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_board()

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j].config(text="")
        self.current_player = "X"
        self.computer_turn = False

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
