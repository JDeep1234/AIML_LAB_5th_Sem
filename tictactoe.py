class TicTacToe:
    def __init__(self):
        self.board = [[' ']*3 for _ in range(3)]
        self.player = 'X'

    def print_board(self):
        for row in self.board:
            print(' | '.join(row))
            print('-' * 5)

    def is_draw(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def is_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in zip(*self.board):
            if all(cell == player for cell in col):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2-i] == player for i in range(3)):
            return True
        return False

    def dfs(self, player):
        if self.is_winner('X'):
            return 1  # X wins
        if self.is_winner('O'):
            return -1  # O wins
        if self.is_draw():
            return 0  # Draw

        best_score = -float('inf') if player == 'X' else float('inf')
        move = None
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = player
                    score = self.dfs('O' if player == 'X' else 'X')
                    self.board[i][j] = ' '
                    
                    if (player == 'X' and score > best_score) or (player == 'O' and score < best_score):
                        best_score = score
                        move = (i, j)
        return best_score if move is None else move

    def play(self):
        while True:
            self.print_board()
            if self.is_winner('X') or self.is_winner('O') or self.is_draw():
                print("Game Over.")
                if self.is_winner('X'):
                    print("Player X wins!")
                elif self.is_winner('O'):
                    print("Player O wins!")
                else:
                    print("It's a draw!")
                break

            if self.player == 'X':
                move = self.dfs('X')
                if move:
                    self.board[move[0]][move[1]] = 'X'
            else:
                while True:
                    try:
                        r = int(input("Row (0-2): "))
                        c = int(input("Col (0-2): "))
                        if self.board[r][c] == ' ':
                            self.board[r][c] = 'O'
                            break
                        print("Taken!")
                    except (ValueError, IndexError):
                        print("Invalid!")
            self.player = 'O' if self.player == 'X' else 'X'

if __name__ == '__main__':
    TicTacToe().play()
