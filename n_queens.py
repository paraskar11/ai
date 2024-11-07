def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()

def check_position(board, col, row, n):
    # Check the row
    for j in range(n):
        if board[row][j]:
            return False

    # Check the column
    for i in range(n):
        if board[i][col]:
            return False

    # Check the diagonals
    for i in range(n):
        if (row + col - i) >= n or (row + col - i) < 0:
            continue
        if board[i][row + col - i]:
            return False

    for i in range(n):
        if (i - row + col) >= n or (i - row + col) < 0:
            continue
        if board[i][i - row + col]:
            return False

    return True

def backtracing(board, n, col):
    if col >= n:
        print_board(board, n)
        return True

    for i in range(n):
        if check_position(board, col, i, n):
            board[i][col] = 1
            backtracing(board, n, col + 1)
            board[i][col] = 0

def placeNQueens(n):
    board = [[0] * n for _ in range(n)]
    backtracing(board, n, 0)

# Main function
if __name__ == "__main__":
    placeNQueens(4)

