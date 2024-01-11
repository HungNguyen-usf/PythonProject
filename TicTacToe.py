import tkinter as tk
from tkinter import messagebox
import random


def check_win():
    global board

    # Check rows for a win
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != "-":
            return True

    # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "-":
            return True

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return True

    return False


def check_draw():
    for row in range(3):
        for col in range(3):
            if board[row][col] == "-":
                return False
    return True


def make_move(row, col):
    global player, board, single_player

    if board[row][col] == "-":
        board[row][col] = player
        buttons[row][col].config(text=player)

        # Check for win or draw
        if check_win():
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            reset_board()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()

        # Switch to the other player
        player = "X" if player == "O" else "O"

        # If single-player and it's AI's turn, make AI move
        if single_player and player == "O":
            ai_move()


def ai_move():
    global board

    # Get a list of empty cells
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == "-"]

    if empty_cells:
        # Select a random empty cell for AI move
        row, col = random.choice(empty_cells)
        make_move(row, col)


def create_board():
    buttons = [[None for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            button = tk.Button(root, text="-", font=("Arial", 20), width=5, height=2,
                               command=lambda r=row, c=col: make_move(r, c))
            button.grid(row=row, column=col)
            buttons[row][col] = button
    return buttons


def reset_board():
    global board, player
    for row in range(3):
        for col in range(3):
            board[row][col] = "-"
            buttons[row][col].config(text="-")
    player = "X"


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tic Tac Toe")
    root.geometry("300x300")

    single_player = True  # Set to False for two-player mode
    player = "X"
    board = [["-" for _ in range(3)] for _ in range(3)]
    buttons = create_board()

    root.mainloop()