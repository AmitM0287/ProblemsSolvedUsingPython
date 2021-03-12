# ----- Global Variables -----

# Who won or tie?
winner = None

# If game is still going
game_still_going = True

# Who's turn is it?
current_player = 'X'

# Game Board
board = ['_', '_', '_', '_',
         '_', '_', '_', '_',
         '_', '_', '_', '_']


# Play a game of tic tac toe
def play_game():
    # Display initial board
    display_board()
    # While the game is still going
    while game_still_going:
        # Handle a single turn of an arbitrary player
        handle_turn(current_player)
        # Flip to the other player
        flip_player()
        # Check if game has ended
        check_if_game_over()


# Display Board
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# Handle a single turn of an arbitrary player
def handle_turn(player):
    print(player + "'s turn.")
    position = input('Choose a position from 1-9:')

    while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        position = input('Invalid Input. Choose a position from 1-9:')

    position = int(position) - 1
    board[position] = player
    display_board()


# Check if game is over
def check_if_game_over():
    check_for_winner()
    check_if_tie()


# Flip Player
def flip_player():
    # Global variables we need
    global current_player
    # If current player was X, then change it to O
    if current_player == 'X':
        current_player = 'O'
    # If current player was O, then change it to X
    elif current_player == 'O':
        current_player = 'X'


# Check for winner
def check_for_winner():
    # Set up global variables
    global winner
    # Check rows
    row_winner = check_rows()
    # Check columns
    column_winner = check_columns()
    # Check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# Check if tie
def check_if_tie():
    global game_still_going
    if '_' not in board:
        game_still_going = False


# Check row wise
def check_rows():
    # Set up global variables
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    row1 = board[0] == board[1] == board[2] != '_'
    row2 = board[3] == board[4] == board[5] != '_'
    row3 = board[6] == board[7] == board[8] != '_'
    # If any row does have a match, flag that there is a win
    if row1 or row2 or row3:
        game_still_going = False
    # Return the winner (X or O)
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]


# Check column wise
def check_columns():
    # Set up global variables
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    column1 = board[0] == board[3] == board[6] != '_'
    column2 = board[1] == board[4] == board[7] != '_'
    column3 = board[2] == board[5] == board[8] != '_'
    # If any column does have a match, flag that there is a win
    if column1 or column2 or column3:
        game_still_going = False
    # Return the winner (X or O)
    if column1:
        return board[0]
    if column2:
        return board[1]
    if column3:
        return board[2]


# Check diagonal wise
def check_diagonals():
    # Set up global variables
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    diagonal1 = board[0] == board[4] == board[8] != '_'
    diagonal2 = board[6] == board[4] == board[2] != '_'
    # If any diagonals does have a match, flag that there is a win
    if diagonal1 or diagonal2:
        game_still_going = False
    # Return the winner (X or O)
    if diagonal1:
        return board[0]
    if diagonal2:
        return board[6]


if __name__ == '__main__':
    # Start Playing
    play_game()

    # The game has ended
    if winner == 'X' or winner == 'O':
        print(winner, ' won.')
    elif winner is None:
        print('Tie.')
