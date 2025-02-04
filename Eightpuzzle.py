import numpy as np
from queue import PriorityQueue

def solve_puzzle(start, goal):
    def h(s): return np.sum(s != goal)  # Count misplaced tiles
    
    queue = PriorityQueue()
    queue.put((h(start), start.tobytes(), []))
    visited = set()
    
    while not queue.empty():
        _, state_bytes, path = queue.get()
        state = np.frombuffer(state_bytes, dtype=int).reshape(3, 3)
        
        if np.array_equal(state, goal): return path + [state]
        visited.add(state_bytes)
        
        x, y = np.argwhere(state == 0)[0]
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = state.copy()
                new_state[x, y], new_state[nx, ny] = new_state[nx, ny], 0
                new_bytes = new_state.tobytes()
                
                if new_bytes not in visited:
                    queue.put((h(new_state), new_bytes, path + [state]))
    return None

start = np.array([[2, 8, 1], [0, 4, 3], [7, 6, 5]])
goal = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

solution = solve_puzzle(start, goal)
if solution:
    for step in solution: print(step)
    print("Moves:", len(solution) - 1)
else:
    print("No solution!")
