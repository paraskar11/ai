# Tic-Tac-Toe board initialization
board = [' ' for _ in range(9)]  # A list to hold the board's current state
current_player = 'X'  # X always starts

# Display the Tic-Tac-Toe board
def display_board():
    print(f"\n {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}\n")

# Recursive function to check for a win
def check_win(player, board, index=0):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal lines
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical lines
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    
    # Base case: If we have checked all win conditions
    if index >= len(win_conditions):
        return False
    
    # Check if the current win condition holds for the player
    if all(board[i] == player for i in win_conditions[index]):
        return True
    
    # Recursive call to check the next win condition
    return check_win(player, board, index + 1)

# Function to check if the board is full (i.e., it's a draw)
def check_draw():
    return all(spot != ' ' for spot in board)

# Function to handle player moves
def player_move(player):
    move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = player
    else:
        print("Invalid move! Try again.")
        player_move(player)  # Recursive call for valid move

# Function to switch players
def switch_player(player):
    return 'O' if player == 'X' else 'X'

# Recursive function to play the game
def play_game(player):
    display_board()
    
    # Player makes a move
    player_move(player)
    
    # Check if the current player has won
    if check_win(player, board):
        display_board()
        print(f"Player {player} wins!")
        return  # End the game
    
    # Check if the game is a draw
    if check_draw():
        display_board()
        print("It's a draw!")
        return  # End the game
    
    # Switch to the other player and continue the game recursively
    play_game(switch_player(player))

# Start the game
play_game(current_player)
# TC:O(b^d)
# SC:(b)
