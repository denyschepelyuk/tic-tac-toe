# User Documentation for a Python Tic-Tac-Toe Program

## Logical Part of the Program

My program has a bunch of functions, responsible for changing the game state and checking players’ inputs. It contains such functions as:

- **resetGame()**: Responsible for starting the game over.
- **findEmpty()**: Checks if there are any empty tiles.
- **winnerTiles()**: Checks if any player has managed to put three signs in a single row/column/diagonal and returns such tiles or `None` if there is no winner.
- **gameState()**: Checks what state the game is currently in (it continues/some player has won/it is a draw). Uses `findEmpty()` and `winnerTiles()` functions.
- **paintTie()**: Sets the color of all buttons to yellow (used when the game is a draw).
- **paintWinningTiles(win_ties)**: Sets the color of buttons from array `win_ties` to green (used to highlight the tiles a player filled to win).
- **switchPlayer(prev_player)**: Returns the player different from `prev_player` (useful for quickly swapping players).
- **update_board()**: Operates with some previously mentioned functions to display relevant information depending on the state of the game and paint tiles if needed.
- **playersMove(row, column)**: Places the player's sign on the tile they pressed if possible.
- **minimax(isMaximizing, prev_player, alpha, beta)**: Tries to play all possible moves to find the best one.
- **getHint()**: Calculates the best possible move considering the current situation on the board and places the next player's sign on that tile (uses `minimax()` function).

## The Course of the Game

Two players move in turn. The first player to move is chosen at random. The game will continue until one of the following cases occurs: a tie or someone's win. Moves occur as follows:

1. The player presses the button (tile) they want to place their sign into.
2. The button calls the function `playersMove()`.
3. The function `playersMove()` checks if the move is possible and if the game state allows making moves:
    - If so, the sign will be placed there and it will be the other player’s move.
    - Otherwise, nothing happens and the game continues with the same player to move.

### Win Conditions

A player wins when they manage to put three symbols in one row, column, or diagonal.

### Tie Conditions

A tie occurs when no player has won, but there are no possible moves left as the board is full.

### Board Updates

After any change to the board (tiles), the function `update_board()` will be called to update information about the next player or other information according to the current game state:

- **If there is a winner**: The function will set the top label to show who has won and will highlight the tiles the player filled to win with green color.
- **If there is no winner but not all tiles are filled yet**: The function will update the top label to show which player is next to move.
- **If there is no winner and all tiles are filled**: The function will set the top label to show that it is a draw and paint all tiles in yellow.

### Using Hints

At any moment of the game, each player can take a hint by pressing the hint button. After pressing it, the player's sign will be placed automatically at the best place (the bot will make the best possible move) and the game will continue as usual with the other player to move now. The hint button calls the function `getHint()` which simulates all possible game outcomes and makes the move most likely to lead to a win. It uses the minimax algorithm with alpha-beta pruning to find the best move according to the board state when the hint was called.

### Resetting the Game

At any moment of the game, the reset button can be pressed, whereupon the board will be cleared and the game starts over. To perform this operation, the program calls the `resetGame()` function which resets all buttons to their initial state and randomly chooses the first player to start the game.

## GUI Part of the Program

In this project, a built-in library Tkinter is used to make the GUI. Also, the button from the tkmacosx library was used because the button object wasn’t fully adjustable on MacOS without it. 

In the project, only a few objects from Tkinter were used as the interface is pretty simple and minimalistic:

- **Label**: Used for the top text and packed at the top of the window.
- **Buttons**: Used for auxiliary controls to reset and hint. These buttons are packed on the left and right sides of the window respectively.
- **Frame**: Contains 9 buttons (game board) at the bottom of the window. The frame's purpose is to place buttons in a specific and precise order (square-shaped 3x3).
