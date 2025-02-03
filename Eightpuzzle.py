import numpy as np
from queue import PriorityQueue

class Puzzle:
    def __init__(self, start, goal): self.s, self.g = start, goal
    def show(self, grid): print(grid)
    def is_goal(self, grid): return np.array_equal(grid, self.g)
    def moves(self, grid):
        p = np.argwhere(grid == 0)[0]
        mv = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        return [self.swap(grid, p, (p[0]+dx, p[1]+dy)) for dx, dy in mv if 0 <= p[0]+dx < 3 and 0 <= p[1]+dy < 3]
    def swap(self, grid, p1, p2):
        g = grid.copy()
        g[p1[0], p1[1]], g[p2[0], p2[1]] = g[p2[0], p2[1]], g[p1[0], p1[1]]
        return g
    def heuristic(self, grid): return np.sum(grid != self.g)
    def solve(self):
        pq, seen = PriorityQueue(), set()
        pq.put((self.heuristic(self.s), self.s.tobytes(), [self.s]))  # Use tobytes for comparison
        while not pq.empty():
            _, state_key, path = pq.get()
            cur = np.frombuffer(state_key, dtype=int).reshape(3, 3)
            if self.is_goal(cur): return path
            for move in self.moves(cur):
                m_key = move.tobytes()
                if m_key not in seen:
                    seen.add(m_key)
                    pq.put((self.heuristic(move) + len(path), m_key, path + [move]))  # Add path length to heuristic
        return None

start = np.array([[2, 8, 1], [0, 4, 3], [7, 6, 5]])
goal = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
p = Puzzle(start, goal)
res = p.solve()

if res:
    for i, step in enumerate(res): print(f"Move {i}:\n{step}\n")
    print(f"Total moves: {len(res)-1}")
else: print("No solution found.")
