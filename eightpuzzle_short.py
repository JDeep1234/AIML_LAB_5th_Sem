import numpy as np
from queue import PriorityQueue

def solve_puzzle(start, goal):
    def h(s): return np.sum(s != goal)  # Count misplaced tiles
def manhattan_distance(state, goal):
    """Calculate Manhattan distance heuristic."""
    distance = 0
    for num in range(1, 9):  # Ignore 0 (empty space)
        x1, y1 = np.argwhere(state == num)[0]
        x2, y2 = np.argwhere(goal == num)[0]
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def get_neighbors(state):
    """Generate valid moves for the empty tile (0)."""
    x, y = np.argwhere(state == 0)[0]
    neighbors = []
    moves = {'Right': (0,1), 'Down': (1,0), 'Left': (0,-1), 'Up': (-1,0)}

    for move, (dx, dy) in moves.items():
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = state.copy()
            new_state[x, y], new_state[nx, ny] = new_state[nx, ny], 0
            neighbors.append((move, new_state))
    return neighbors

def solve_puzzle(start, goal):
    """A* algorithm to solve the 8-puzzle problem."""
    queue = PriorityQueue()
    queue.put((h(start), start.tobytes(), []))
    queue.put((manhattan_distance(start, goal), 0, start, []))  # (f, g, state, path)
    visited = set()
    

    while not queue.empty():
        _, state_bytes, path = queue.get()
        state = np.frombuffer(state_bytes, dtype=int).reshape(3, 3)
        f, g, state, path = queue.get()
        state_tuple = tuple(map(tuple, state))  # Convert to hashable format

        if np.array_equal(state, goal): return path + [state]
        visited.add(state_bytes)
        if np.array_equal(state, goal):
            return path  # Return solution path

        x, y = np.argwhere(state == 0)[0]
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = state.copy()
                new_state[x, y], new_state[nx, ny] = new_state[nx, ny], 0
                new_bytes = new_state.tobytes()
                
                if new_bytes not in visited:
                    queue.put((h(new_state), new_bytes, path + [state]))
        visited.add(state_tuple)

        for move, new_state in get_neighbors(state):
            new_tuple = tuple(map(tuple, new_state))
            if new_tuple not in visited:
                queue.put((g + 1 + manhattan_distance(new_state, goal), g + 1, new_state, path + [move]))

    return None

start = np.array([[2, 8, 1], [0, 4, 3], [7, 6, 5]])
goal = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
def input_puzzle():
    """Take user input for 3x3 puzzle state."""
    print("Enter the puzzle as a 3x3 grid (use 0 for the empty space):")
    matrix = []
    for i in range(3):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

# Get input from user
print("Enter the START state:")
start = input_puzzle()

print("Enter the GOAL state:")
goal = input_puzzle()

# Solve the puzzle
solution = solve_puzzle(start, goal)

# Output result
if solution:
    for step in solution: print(step)
    print("Moves:", len(solution) - 1)
    print("\nSolution Found!")
    print("Moves:", solution)
    print("Total Moves:", len(solution))
else:
    print("No solution!")
    print("\nNo solution exists for this configuration!")
