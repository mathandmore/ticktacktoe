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
    
    
    print_board(board2)
    print("\n\n\n\n\n\n\n")
    board2[1][0]=3
    print_board(board2)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    cs()
    for game in range(0,9):
        print_board(board2)
        print(game)
        if game%2 == 0 or game == 0:
            
             
            symbl = "x"
            play = int(input(f"Player {symbl} choose spot 1-9"))
            if play == 1:
                r = 0
                c = 0
                board2[r][c]="✕"
            elif play == 2:
                r = 0
                c = 1
                board2[r][c]="✕"
            elif play == 3:
                r = 0
                c = 2
                board2[r][c]="✕"
            elif play == 4:
                r = 1
                c = 0
                board2[r][c]="✕"
            elif play == 5:
                r = 1
                c = 1
                board2[r][c]="✕"
            elif play == 6:
                r = 1
                c = 2
                board2[r][c]="✕"
            elif play == 7:
                r = 2
                c = 0
                board2[r][c]="✕"
            elif play == 8:
                r = 2
                c = 1
                board2[r][c]="✕"
            else:
                r = 2
                c = 2
                board2[r][c]="✕"

                
                
        
        
        
        else:
            symbl = "o"
            play = int(input(f"Player {symbl} choose spot 1-9"))

            if play == 1:
                r = 0
                c = 0
                board2[r][c]="⚬"
            elif play == 2:
                r = 0
                c = 1
                board2[r][c]="⚬"
            elif play == 3:
                r = 0
                c = 2
                board2[r][c]="⚬"
            elif play == 4:
                r = 1
                c = 0
                board2[r][c]="⚬"
            elif play == 5:
                r = 1
                c = 1
                board2[r][c]="⚬"
            elif play == 6:
                r = 1
                c = 2
                board2[r][c]="⚬"
            elif play == 7:
                r = 2
                c = 0
                board2[r][c]="⚬"
            elif play == 8:
                r = 2
                c = 1
                board2[r][c]="⚬"
            else:
                r = 2
                c = 2
                board2[r][c]="⚬"
            


ttt()
🗺
