import time as t
import random
import os

def cs():
    if os.name == 'nt':  
        _ = os.system('cls')
    else:  
        _ = os.system('clear')
cs()

def print_board(board):
    for row in range(3):
        v = ""
        for col in range(3):
            v += f"| {board[row][col]} |"
        print(v)
            
def ttt():
    
    board2 = [
        ["1","2","3"],
        ["4","5","6"],
        ["7","8","9"]
    ]
    
    cs()
    for game in range(0,9):
        cs()
        print_board(board2)
        print(game)

        if game%2 == 0:
            symbl = "✕"
        else:
            symbl = "o"
            
        while True:
                play  = int(input(f"Player {symbl} choose spot 1-9"))
                if play > 9 or play <1:
                    print("Sorry try again")
                    continue 
                
                r = (play-1)//3
                c = (play-1)%3
                if board2[r][c] == "⚬" or board2[r][c] == "✕":
                    print("Sorry try again")
                    continue

                else:
                    board2[r][c] = symbl
                    #TODO win detection 
                    break

ttt()
