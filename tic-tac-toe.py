from tkinter import *
from tkmacosx import Button
import random

def resetGame():
    label.config(text = (random.choice(players) + "'s turn"))
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = ""
            signs[i][j] = ''
            buttons[i][j].config(bg = "white")

def findEmpty():
    for i in range(3):
        for j in range(3):
            if signs[i][j] == "":
                return True
    return False

def winnerTiles():

    global buttons

    for i in range(3):

        if signs[i][0] == signs[i][1] == signs[i][2] != "":
            return [ buttons[i][0], buttons[i][1], buttons[i][2] ]
        
        elif signs[0][i] == signs[1][i] == signs[2][i] != "":
            return [ buttons[0][i], buttons[1][i], buttons[2][i] ]
    
    if signs[0][0] == signs[1][1] == signs[2][2] != "":
        return [ buttons[0][0], buttons[1][1], buttons[2][2] ]
        
    if signs[2][0] == signs[1][1] == signs[0][2] != "":
        return [ buttons[2][0], buttons[1][1], buttons[0][2] ]
    
    return None

def gameState():

    if winnerTiles() != None:
        return "win"

    if findEmpty():
        return "ongoing"
    
    return "tie"

def paintTie():

    global buttons

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(bg = "yellow")

def paintWinningTiles(win_ties):
    for i in win_ties:
        i.config(bg = "green")

def oppositePlayer(prev_player):
    if (prev_player == players[0]):
        return players[1]
    else:
        return players[0]

def update_board():

    game_state = gameState()
    prev_player = oppositePlayer(next_player)

    if game_state == "ongoing":
        label.config(text = (next_player + " next"))

    elif game_state == "tie" :
        label.config(text = ("Tie!"))
        paintTie()
            
    elif game_state == "win":
        label.config(text = (prev_player + " wins"))
        paintWinningTiles(winnerTiles())

def playersMove(row, column):
    
    global next_player

    if signs[row][column] == "" and gameState() == "ongoing":

        buttons[row][column]['text'] = next_player
        signs [row][column] = next_player

        next_player = oppositePlayer(next_player)
        
        update_board()
        

def minimax(isMaximizing, prev_player, alpha, beta):

    global signs

    tmp_player = oppositePlayer(prev_player)

    if gameState() == "win":
        if not isMaximizing:
            return 1
        elif isMaximizing:
            return -1
    elif gameState() == "tie":
        return 0

    if isMaximizing:
        bestScore = -1
        for i in range(3):
            for j in range(3):
                if beta <= alpha:
                    return bestScore
                if signs[i][j] == '':
                    signs[i][j] = tmp_player
                    score = minimax(False, tmp_player, alpha, beta)
                    signs[i][j] = ''
                    bestScore = max(bestScore, score)
                    alpha = max(alpha, score)
        return bestScore
    else:
        bestScore = 1
        for i in range(3):
            for j in range(3):
                if beta <= alpha:
                    return bestScore
                if signs[i][j] == '':
                    signs[i][j] = tmp_player
                    score = minimax(True, tmp_player, alpha, beta)
                    signs[i][j] = ''
                    bestScore = min(bestScore, score)
                    beta = min(beta, score)
                    
        return bestScore

def getHint():

    if gameState() != "ongoing":
        return

    global buttons
    global next_player

    bestScore = -1
    tmp_player = next_player
    bestMove = None
 
    for i in range(3):
        for j in range(3):
            if signs[i][j] == '':
                signs[i][j] = tmp_player
                score = minimax(False, tmp_player, -1, 1)
                signs[i][j] = ''
                if score >= bestScore:
                    bestScore = score
                    bestMove = [i, j]

    buttons[bestMove[0]][bestMove[1]]['text'] = tmp_player
    signs[bestMove[0]][bestMove[1]] = tmp_player

    next_player = oppositePlayer(next_player)

    update_board()

    

window = Tk()
window.title("Tic-Tac-Toe")

players = ['O', 'X']
next_player = random.choice(players)

label = Label(text = next_player + "'s turn", font = ('Arial, 35'))
label.pack(side = 'top')

buttons_frame = Frame(window)
buttons_frame.pack()

reset_button = Button(buttons_frame, text = "reset", font = ('Arial, 18'), command = resetGame)
reset_button.pack(side = "left")

hint_button = Button(buttons_frame, text = "hint", font = ('Arial', 18), command = getHint)
hint_button.pack(side = "right")


frame = Frame(window)
frame.pack()

buttons = [[0,0,0], [0,0,0], [0,0,0]]
signs = [ ['', '', ''], ['', '', ''], ['', '', '']]

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text = "", font = ('Arial, 35'), width = 120, height = 120, command = lambda row = row, column = column: playersMove(row, column))
        buttons[row][column].grid(row = row, column = column)

window.mainloop()