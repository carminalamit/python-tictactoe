'''How do you play the game tic-tac-toe?
1. The game is played on a grid that's 3 squares by 3 squares.
2. You are X, your friend (or the computer in this case) is O. Players take turns putting their marks in empty squares.
3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
4. When all 9 squares are full, the game is over.'''

print('''\033[1;32m⠠⠤⠤⠴⠶⠖⣦⠄⠄⠄⠄⢀⣀⡀⠄⡶⠶⠦⠤⠤⢤⡀⠄⠄⠄⠄⠄⢀⣀⣀⣀⠄⡴⠶⠒⠚⠋⢹⠄⠄⣀⡀⠄⠄⠄⣀⡀⠄⠄⠄
⣾⠄⠄⠄⠄⠄⡟⠒⠒⣦⠞⠉⠉⢹⣰⠇⠄⠄⠄⠄⢰⠷⠖⠒⣆⢠⡞⠉⠄⠄⢸⣷⡇⠄⠄⠄⠄⣸⠖⠉⠉⠉⠉⢲⣸⠉⠉⠉⠉⣶
⣷⣶⡆⠄⠄⡶⡇⠄⠄⠃⠄⢀⣤⣼⡿⠶⡆⠄⠄⣶⣾⠄⠄⠄⠹⡞⠄⠄⣴⣶⣼⡿⠷⢶⠄⠄⢸⡏⠄⢀⣤⣄⠄⠄⢻⠄⠄⣤⣤⣸
⠄⠘⡇⠄⠄⣧⡇⠄⢰⠄⠄⢸⠁⠈⠄⠄⡇⠄⠄⣿⡇⠄⢸⠄⠄⡇⠄⠄⣇⠄⠈⠄⠄⢸⡀⠄⠘⡇⠄⢸⡃⢹⠆⠄⠸⠄⠄⠄⢸⠉
⠄⠄⡇⠄⠄⣿⡇⠄⢸⡄⠄⠈⠓⠋⡇⢠⡇⠄⠄⣿⠃⠄⠘⠁⠄⠰⡀⠄⠈⠛⢹⠆⠄⢸⡇⠄⠄⣇⠄⠈⠓⠚⠄⠄⡀⠄⠄⠳⠾⡄
⠄⠄⣧⣀⣀⣿⡇⠄⢸⡿⣦⣀⣀⣀⡇⢸⣇⣀⣀⡿⠄⠄⣤⣤⠄⠄⢳⣤⣀⣀⣾⠄⠄⠄⣇⣀⣤⡿⣦⣀⣀⣀⣀⣼⣇⣀⣀⣀⣰⠇
⠄⠄⠛⠛⠋⠹⠿⠿⠿⠁⠈⠙⠛⠋⠁⠈⠛⠛⠛⣷⣶⣶⡇⠸⠷⠿⠛⠈⠉⠉⠁⠄⠄⠄⠉⠉⠁⠄⠈⠙⠛⠛⠉⠄⠈⠉⠉⠛⠛⠄
\033[1;36m''')

from random import randint

# Initialize global variable
# global variable - Variables that are created outside of a function
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
current_player = "X"
winner = None  
game_running = True 

# printing game board
def print_board(board):
    print(f"\033[33m{board[0]} | {board[1]} | {board[2]}")
    print("\033[33m---------") 
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")


# take player input
def player_input(board):
    inp = int(input("Enter a number 1-9: "))
    # expression to make sure input is valid 
    if inp >= 1 and inp <=9 and board[inp-1] == "-":
        board[inp-1] = current_player
    else:
        print("Oops player is already at that spot.")
 

# Check for win or tie on each angle 
# check on horizontal
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

# check on vertical
def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True

# check on diagonal 
def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True

def check_tie(board):
    # Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
    # If you use the global keyword, the variable belongs to the global scope
    global game_running
    if "-" not in board:
        print_board(board)
        print("It is a tie!")
        game_running = False

def check_win():
    if check_diagonal(board) or check_horizontal(board) or check_vertical(board):
        print(f"The winner is {winner}")

# switch the player
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# computer
# ability for a computer to make some move
def computer(board):
    while current_player == "O":
        position = randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switch_player()

# check for win and tie again
while game_running:
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()
    computer(board)
    check_win()
    check_tie(board)
    