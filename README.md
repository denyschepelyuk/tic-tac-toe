This is a user documentation for a python

tic-tac-toe program.

Logical part of the program:
My program has a bunch of functions, responsible for changing the game state and checking
players’ inputs.
It contains such functions as:
● resetGame() - responsible for starting the game over
● findEmpty() - checks if there are any empty tiles
● winnerTiles() - checks if any player has managed to put three signs in a single
row/column/diagonal and returns such tiles or None value if there is no winner
● gameState() - checks what state is game currently in (it continues/ some player has
won/ it is a drow) (uses findEmpty(), findWinner() functions)
● paintTie() - sets the color of all buttons to yellow (is used when the game is in a draw)
● paintWinningTiles(win_ties) - sets the color of buttons from array win_ties to green (is
used to highlight the ties, player filled to win)
● switchPlayer(prev_player) - returns the player, different to prev_player (is very useful
as the program usually need to quickly swap the player
● update_board() - functions which operates with some previously mentioned
functions, to display relevant information, depending on the state of the game and
paint tiles if needed
● playersMove(row, column) - function which places players sign on tile at which player
pressed if possible
● minimax(isMaximizing, prev_player, alpha, beta) - function which tries to play all
possible perspective moves to find out which one is the best to play
● getHint() - function which calculates best possible move considering current situation
on a board and places next player's sign in such tile (uses minimax() function)

The course of the game:

Two players move in turn. The first player to move is chosen at random. Game will continue
until one of the cases occurs: a tie or someone's win.
Moves occur as follows:
1. player presses the button (tile) he want place his sign into
2. button then calls the function playersMove()
3. function playersMove() checks if move is possible and if the game state allows to
make moves
a. if so, sign will be placed there and now it will be other player’s move
b. otherwise nothing happens and the game continues with the same player to
move

Win comes when the player manages to put three symbols in one row column or diagonal.
Tie is a state of the game, when no player has won, but there are no possible moves as the
board is full.
After any board (tiles) change function update_board() will be called to update information
about next player or the other information according to the current game state:
A. if there is a winner: function will set the top label to show who has won and will
highlight tiles player filled to win with green color
B. if there is no winner but not all tiles are filled yet: function will update the top label that
shows which player is next to move
C. if there is no winner and all tiles are already filled: function will set the top label to
show that it is a draw and paint all tiles in yellow
At any moment of the game each player can take a hint by pressing the hint button. After
pressing it, the player's sign will be placed automatically at the best place (bot will make the
best possible move) and the game will continue as usual with the other player to move now.
Hint button calls the function getHint() which simulates all possible variants of the course of
the game and makes the move, after which the player will most likely win the game.
It uses the minimax algorithm with alpha-beta pruning to find the best possible move
according to the board state when the hint was called. Alpha-beta pruning is used to
decrease the time of the operation by ignoring moves which are not promising compared to
those calculated earlier.
Similarly at any moment of the game reset button can be pressed whereupon the board will
be cleared, and the game starts over.
To perform this operation the program calls resetGame() function which resets all buttons to
initial state and randomly chooses the first player to start the game.

GUI part of the program:
In this project a built-in library Tkinter is used to make GUI. Also button from
tkmacosx library was used for the reason that button object wasn’t fully adjustable on
MacOs without it.
In the project only few objects from tkinter were used as the interface is pretty simple
and minimalistic.
● Label was used for the top text and therefore was packed at the top of the
window.
● Under the text there are auxiliary buttons to control the progress of the game
reset and hint. Button objects were used here, and the buttons are packed on
the left and right sides of the window respectively.
● On the bottom of the window is a frame which contains 9 buttons (game
board). The only purpose of the frame is to place buttons in more specific and
precise order (square shaped 3x3).