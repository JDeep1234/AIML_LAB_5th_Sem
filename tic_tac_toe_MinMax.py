#THE FIRST CODE: TIC TAC TOE
l = []
def tictactoe(board, turn, flag):

    maximum = -100000
    minimum = 100000
    count = 0
    
    if hasWon(board, 'X'):
        return 1, None  # AI wins
    if hasWon(board, 'O'):
        return -1, None  # Player wins
    if isDraw(board):
        return 0, None  # Draw
    
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                if turn == 0:#IT IS Xs turn to play
                    board[i][j] = 'X'
                    count = tictactoe(board, 1 - turn, 1)[0]
                    board[i][j] = '.'
                    if maximum < count:
                        maximum = count
                        best_move = (i, j)
                    maximum = max(maximum, count)
                else:
                    board[i][j] = 'O'
                    count = tictactoe(board, 1 - turn, 1)[0]
                    if minimum > count:
                        minimum = count
                        best_move = (i, j)
                        
                    board[i][j] = '.'
                    minimum = min(minimum, count)
        
    if turn == 1:
        return minimum, best_move
    return maximum, best_move

def isDraw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                return False
    return True

def hasWon(board, turn):
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] == turn):
            return True
    for i in range(3):
        if (board[0][i] == board[1][i] == board[2][i] == turn):
            return True    
    #do the diagonall check
    if board[0][0] == board[1][1] == board[2][2] == turn:
        return True
    if board[0][2] == board[1][1] == board[2][0] == turn:
        return True
    return False

def printBoard(board):
    for i in range(3):
        print(str(board[i][0]) + " " + str(board[i][1]) + " " + str(board[i][2]))
    
board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
def simulate():
    turn = 1    #AI STARTS FIRST
    while True:
        if turn == 0:
            row, col = tictactoe(board, 0, 0)[1]
            
            board[row][col] = 'X'
            printBoard(board)
            if hasWon(board, 'X'):
                print("AI WON THE GAME")
                break
            turn = 1 - turn
        else:
            t = input('ENTER COORDINATES:')
            r = int(t.split()[0])
            c = int(t.split()[1])
            board[r][c] = 'O'
            printBoard(board)
            if hasWon(board, 'O'):
                print("YOU WON THE GAME")
                break
            turn = 1 - turn 
        print()
        if isDraw(board):
            print("GAME IS DRAW")
            break

simulate()
