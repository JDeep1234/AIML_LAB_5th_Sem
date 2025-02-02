import numpy as np
from queue import PriorityQueue

class State:
    def __init__(self, grid, parent):
        self.grid = grid
        self.parent = parent

    def __lt__(self, other):
        return False  # Dummy comparison for PriorityQueue

class Puzzle:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def show(self, grid):
        print(grid)

    def is_goal(self, grid):
        return np.array_equal(grid, self.goal)

    def moves(self, grid):
        pos = np.argwhere(grid == 0)[0]
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        next_moves = []
        for dx, dy in steps:
            x, y = pos[0] + dx, pos[1] + dy
            if 0 <= x < 3 and 0 <= y < 3:
                new_grid = grid.copy()
                new_grid[pos[0], pos[1]], new_grid[x, y] = new_grid[x, y], new_grid[pos[0], pos[1]]
                next_moves.append(new_grid)
        return next_moves

    def heuristic(self, grid):
        return np.sum(grid != self.goal)

    def solve(self):
        pq = PriorityQueue()
        start_state = State(self.start, None)
        pq.put((0, start_state))
        seen = set()

        while not pq.empty():
            _, current = pq.get()
            if self.is_goal(current.grid):
                return current
            for move in self.moves(current.grid):
                if str(move) not in seen:
                    seen.add(str(move))
                    pq.put((self.heuristic(move), State(move, current)))
        return None

# Test the solver
start = np.array([[2, 8, 1], [0, 4, 3], [7, 6, 5]])
goal = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

puzzle = Puzzle(start, goal)
result = puzzle.solve()

if result:
    steps = []
    while result:
        steps.append(result.grid)
        result = result.parent
    steps.reverse()
    for i, step in enumerate(steps):
        print(f"Move {i}:")
        puzzle.show(step)
    print(f"Total moves: {len(steps) - 1}")
else:
    print("No solution found.")
