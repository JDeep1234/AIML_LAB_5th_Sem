class TicTacToe:
    def __init__(self):
        self.board = [[' ']*3 for _ in range(3)]
        self.player = 'X'

    def print_board(self):
        print('\n'.join([' | '.join(row) for row in self.board]) + '\n')

    def is_game_over(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ': return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ': return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ': return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ': return self.board[0][2]
        return False

    def is_draw(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def dfs(self, board, player):
        winner = self.is_game_over()
        if winner: return {'score': 1 if winner == 'X' else -1}
        if self.is_draw(): return {'score': 0}

        best = {'score': -float('inf')} if player == 'X' else {'score': float('inf')}
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player
                    score = self.dfs(board, 'O' if player == 'X' else 'X')
                    board[i][j] = ' '
                    score['row'], score['col'] = i, j
                    if (player == 'X' and score['score'] > best['score']) or (player == 'O' and score['score'] < best['score']):
                        best = score
        return best

    def play(self):
        while True:
            self.print_board()
            winner = self.is_game_over()
            if winner or self.is_draw():
                print(f"Player {winner} wins!" if winner else "It's a draw!")
                break

            if self.player == 'X':
                print("AI is making a move...")
                move = self.dfs(self.board, 'X')
                self.board[move['row']][move['col']] = 'X'
            else:
                while True:
                    try:
                        row, col = map(int, input("Enter row and column (0-2): ").split())
                        if self.board[row][col] == ' ':
                            self.board[row][col] = 'O'
                            break
                        print("Invalid move. Try again.")
                    except (ValueError, IndexError):
                        print("Invalid input.")

            self.player = 'O' if self.player == 'X' else 'X'

TicTacToe().play()
