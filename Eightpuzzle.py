import numpy as np
from queue import PriorityQueue

class Puzzle:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def show(self, grid):
        print(grid)

    def is_goal(self, grid):
        return np.array_equal(grid, self.goal)

    def moves(self, grid):
        """Generate possible moves by swapping the empty tile (0) with adjacent tiles."""
        empty_pos = np.argwhere(grid == 0)[0]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        return [
            self.swap(grid, empty_pos, (empty_pos[0] + dx, empty_pos[1] + dy))
            for dx, dy in directions
            if 0 <= empty_pos[0] + dx < 3 and 0 <= empty_pos[1] + dy < 3
        ]

    def swap(self, grid, p1, p2):
        """Swap two positions in the grid to simulate a move."""
        new_grid = grid.copy()
        new_grid[p1[0], p1[1]], new_grid[p2[0], p2[1]] = new_grid[p2[0], p2[1]], new_grid[p1[0], p1[1]]
        return new_grid

    def heuristic(self, grid):
        """Heuristic: Count misplaced tiles compared to the goal."""
        return np.sum(grid != self.goal)

    def solve(self):
        """A* Search Algorithm to find the optimal solution."""
        pq = PriorityQueue()
        visited = set()
        
        start_key = self.start.tobytes()
        pq.put((self.heuristic(self.start), start_key, [self.start]))
        
        while not pq.empty():
            _, state_key, path = pq.get()
            current_state = np.frombuffer(state_key, dtype=int).reshape(3, 3)
            
            if self.is_goal(current_state):
                return path  # Solution found

            for move in self.moves(current_state):
                move_key = move.tobytes()
                if move_key not in visited:
                    visited.add(move_key)
                    pq.put((self.heuristic(move) + len(path), move_key, path + [move]))  # f = g + h

        return None  # No solution found

# Define the start and goal states
start = np.array([[2, 8, 1], [0, 4, 3], [7, 6, 5]])
goal = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

# Solve the puzzle
puzzle = Puzzle(start, goal)
solution = puzzle.solve()

# Display the result
if solution:
    for i, step in enumerate(solution):
        print(f"Move {i}:\n{step}\n")
    print(f"Total moves: {len(solution) - 1}")
else:
    print("No solution found.")
