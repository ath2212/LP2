def isSafe(board, row, col):
    n_rows = len(board)
    n_cols = len(board[0])
    for i in range(n_rows):
        if board[i][col] == 1:
            return False
            
    for j in range(n_cols):
        if board[row][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    # Check lower diagonal on left side
    for i, j in zip(range(row, n_rows, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    return True

def printSolution(board):
    n_rows = len(board)
    n_cols = len(board[0])
    for i in range(n_rows):
        for j in range(n_cols):
            print (board[i][j], end=" ")
        print()

def solve(board, col):
    n_rows = len(board)
    n_cols = len(board[0])
    for i in range(n_rows):
        if col>=n_cols:
            return True
        if isSafe(board, i, col):
            board[i][col] = 1

            if solve(board, col+1):
                #print(col)
                return True
            
            board[i][col] = 0
    return False

board = []
for i in range(8):
    board.append([])
    for j in range(8):
        board[i].append(0)

if solve(board, 0) == False:
    print("Solution doesnt exist")
else:
    printSolution(board)