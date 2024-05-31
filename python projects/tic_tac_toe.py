def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def player_move(board, player):
    while True:
        move = input(f"Player {player}, enter your move (row and column): ").split()
        if len(move) != 2:
            print("Invalid input. Please enter two numbers.")
            continue
        row, col = move
        if not (row.isdigit() and col.isdigit()):
            print("Invalid input. Please enter numbers.")
            continue
        row, col = int(row), int(col)
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Move out of bounds. Try again.")
            continue
        if board[row][col] != " ":
            print("Cell already taken. Try again.")
            continue
        board[row][col] = player
        break

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        player_move(board, current_player)
        
        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

# play_game()




for i in range(1, 101):
    print("wamo")
