import copy  
import heapq as pq  

class Node():  
    def __init__(self, board, h, path):  # Corrected the method name  
        self.board = board  
        self.h = h  
        self.path = path  

    def __lt__(self, other):  # Corrected the method name  
        return self.h < other.h  

def heuristic(board, goal):  
    diff = 0  
    for i in range(3):  
        for j in range(3):  
            if board[i][j] != goal[i][j]:  
                diff += 1  
    return diff  

visited = set()  
q = []  

def calculateSteps(board, goal):  
    pq.heappush(q, Node(board, heuristic(board, goal), [board]))  
    visited.add(str(board))  
    
    while q:  
        node = pq.heappop(q)  
        if heuristic(node.board, goal) == 0:  
            return node.path  
        
        row, col = findZero(node.board)  
        l = [[0, 1], [0, -1], [1, 0], [-1, 0]]  
        
        for i in range(4):  
            temp = copy.deepcopy(node.board)  
            if not (row + l[i][0] == 3 or row + l[i][0] < 0 or col + l[i][1] == 3 or col + l[i][1] < 0):  
                x = temp[row + l[i][0]][col + l[i][1]]  
                temp[row + l[i][0]][col + l[i][1]] = 0  
                temp[row][col] = x  
                if str(temp) not in visited:  
                    visited.add(str(temp))  
                    n = Node(temp, heuristic(temp, goal), [])  
                    n.path = node.path.copy()  
                    n.path.append(temp)  
                    pq.heappush(q, n)  
    return (0, 0)  
        
def findZero(board):  
    for i in range(3):  
        for j in range(3):  
            if board[i][j] == 0:  
                return (i, j)  
    return None  

board = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]  
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  
calculateSteps(board, goal)
