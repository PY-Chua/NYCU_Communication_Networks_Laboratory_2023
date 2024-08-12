# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 15:40:41 2023

@author: 109511286
"""

import tkinter as tk
from tkinter import messagebox

# Create board
def create_board():
    for i in range(3):
        for j in range(3):
            # 建出button
            button = tk.Button(window, text="", font=("Arial", 50), height=2, width=6, command=lambda row=i, col=j: handle_click(row, col))
            button.grid(row=i, column=j, sticky="nsew")

# Handle button clicks
def handle_click(row, col):
    global current_player
    
    # Check which button has been clicked and change player
    if board[row][col] == 0:
        if current_player == 1:
            # 設定board的值
            board[row][col] = "X"
            current_player = 2
        else:
            # 設定board的值
            board[row][col] = "O"
            current_player = 1
        
        # 設定特定row和column的button
        button = window.grid_slaves(row=row, column=col)[0]
        button.config(text=board[row][col])
        
        check_winner()
        
        
# Check for a winner or a tie 檢查遊戲使否結束
def check_winner():
    winner = None
    
    winner_path = []
    
    # Check rows (檢查是否有row連成一線)
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != 0:
            winner = row[0]
            winner_path = [(i, board.index(row)) for i in range(len(row))]
            break

    # Check columns (檢查是否有column連成一線)
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            winner = board[0][col]
            winner_path = [(col, i) for i in range(len(board))]
            break

    # Check diagonals (檢查對角線是否連成一線)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        winner = board[0][0]
        winner_path = [(i, i) for i in range(len(board))]
        
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        winner = board[0][2]
        winner_path = [(i, len(board) - 1 - i) for i in range(len(board))]
    
    # Check if tie (檢查是否平手)
    if all([all(row) for row in board]) and winner is None:
        declare_winner("tie", [])
    
    if winner:
        declare_winner(winner, winner_path)
        
    
# Declare the winner and ask to restart the game
def declare_winner(winner, winner_path):
    # 遊戲平手、整個board變紅色
    if winner == "tie":
        message = "It's a tie!"
        # Change all button colors
        for i in range(3):
            for j in range(3):
                button = window.grid_slaves(row=i, column=j)[0]
                button.config(bg="indianred1")
    # 遊戲有勝負、標出勝利者的連線
    else:
        message = f"Player {winner} wins!"
        # Change button colors for winning path
        for i in winner_path:
            button = window.grid_slaves(row=i[1], column=i[0])[0]
            button.config(bg="lightskyblue")
    # ask if the player wants to continue 視窗詢問玩家是否繼續新一輪遊戲        
    answer = messagebox.askyesno("Game Over", message + " Do you want to restart the game?")
    
    if answer:
        # play another round
        global board
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        for i in range(3):
            for j in range(3):
                button = window.grid_slaves(row=i, column=j)[0]
                button.config(text="", bg=default_bg_color)
                
        global current_player
        current_player = 1
        
    else:
        # close window
        window.destroy()
            
if __name__ == '__main__':
    # create main window 創建主視窗
    window = tk.Tk()
    window.title("Lab3")
    
    # create game board
    create_board()
    default_bg_color = window.cget('bg')
    
    # Initialize variable
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    current_player = 1
    
    window.mainloop()
