class TicTacToe:
    def __init__(self): self.b, self.p = [[' ']*3 for _ in range(3)], 'X'
    def p_b(self): print('\n'.join([' | '.join(r) for r in self.b])+'\n')
    def g_o(self): return any([self.b[i][0]==self.b[i][1]==self.b[i][2]!=' ' for i in range(3)] + [self.b[0][i]==self.b[1][i]==self.b[2][i]!=' ' for i in range(3)] + [self.b[0][0]==self.b[1][1]==self.b[2][2]!=' ', self.b[0][2]==self.b[1][1]==self.b[2][0]!=' '])
    def draw(self): return all(c!=' ' for r in self.b for c in r)
    def dfs(self, p):
        if (w:=self.g_o()): return {'s': 1 if self.p=='X' else -1}
        if self.draw(): return {'s': 0}
        b={'s':-float('inf')} if p=='X' else {'s':float('inf')}
        for i in range(3):
            for j in range(3):
                if self.b[i][j]==' ':
                    self.b[i][j]=p
                    s=self.dfs('O'if p=='X'else'X')
                    self.b[i][j]=' '
                    s['r'],s['c']=i,j
                    if (p=='X'and s['s']>b['s'])or(p=='O'and s['s']<b['s']):b=s
        return b
    def play(self):
        while not (self.g_o() or self.draw()):
            self.p_b()
            if self.p=='X':
                print("AI move...")
                m=self.dfs('X')
                self.b[m['r']][m['c']]='X'
            else:
                while True:
                    try:
                        r,c=map(int,input("Enter row,col (0-2): ").split())
                        if self.b[r][c]==' ':self.b[r][c]='O';break
                        print("Invalid move.")
                    except: print("Invalid input.")
            self.p='O'if self.p=='X'else'X'
        self.p_b()
        print(f"Player {self.g_o()} wins!" if self.g_o() else "It's a draw!")

TicTacToe().play()
