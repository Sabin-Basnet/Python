import tkinter as tk
from tkinter import ttk
from heapq import heappop, heappush

# --- AI CORE LOGIC ---
goal = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
start = ((0, 1, 3), (4, 2, 6), (7, 5, 8))

def misplaced_tiles(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def manhattan_distance(state):
    goal_positions = {
        0: (0, 0), 1: (0, 1), 2: (0, 2),
        3: (1, 0), 4: (1, 1), 5: (1, 2),
        6: (2, 0), 7: (2, 1), 8: (2, 2)
    }
    total_distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:
                goal_i, goal_j = goal_positions[tile]
                total_distance += abs(i - goal_i) + abs(j - goal_j)
    return total_distance

def combined_heuristic(state):
    return misplaced_tiles(state) + manhattan_distance(state)

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
            
def get_neighbors(state):
    x, y = find_blank(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            board = [list(row) for row in state]
            board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
            neighbors.append(tuple(map(tuple, board)))
    return neighbors

def reconstruct(parent, current):
    path = []
    while current is not None:
        path.append(current)
        current = parent[current]
    return path[::-1]

def astar(start, heuristic):
    pq = []
    heappush(pq, (heuristic(start), 0, start))
    parent = {start: None}
    g_cost = {start: 0}
    expanded = 0
    
    while pq:
        f, g, current = heappop(pq)
        expanded += 1
        if current == goal:
            return reconstruct(parent, current), expanded
        
        for neighbor in get_neighbors(current):
            tentative_g = g + 1
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + heuristic(neighbor)
                parent[neighbor] = current
                heappush(pq, (f_cost, tentative_g, neighbor))
    return None, expanded


# --- GUI IMPLEMENTATION ---
class PuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("8-Puzzle AI Solver")
        self.root.geometry("360x500")
        self.root.configure(bg="#2c3e50")
        
        self.path = []
        self.animation_idx = 0
        
        # Grid Title / Stats Label
        self.status_label = tk.Label(
            root, text="Select Heuristic & Click Solve", 
            font=("Helvetica", 12, "bold"), bg="#2c3e50", fg="#ecf0f1"
        )
        self.status_label.pack(pady=15)
        
        # 3x3 Visual Grid Frame (Fixed layout arguments here)
        self.grid_frame = tk.Frame(root, bg="#34495e")
        self.grid_frame.pack(padx=10, pady=10)
        
        self.tiles = [[None for _ in range(3)] for _ in range(3)]
        self.create_grid()
        self.update_grid(start)
        
        # Controls Frame (Dropdown + Button)
        self.controls_frame = tk.Frame(root, bg="#2c3e50")
        self.controls_frame.pack(pady=20)
        
        self.heuristic_var = tk.StringVar(value="h2 (Manhattan)")
        self.dropdown = ttk.Combobox(
            self.controls_frame, textvariable=self.heuristic_var, 
            values=["h1 (Misplaced)", "h2 (Manhattan)", "h1 + h2 (Combined)"],
            state="readonly", width=18
        )
        self.dropdown.grid(row=0, column=0, padx=5, ipady=3)
        
        self.solve_button = tk.Button(
            self.controls_frame, text="Solve!", command=self.solve_puzzle,
            bg="#2ecc71", fg="white", font=("Helvetica", 10, "bold"),
            relief="flat", padx=15, pady=2
        )
        self.solve_button.grid(row=0, column=1, padx=5)

    def create_grid(self):
        for i in range(3):
            for j in range(3):
                label = tk.Label(
                    self.grid_frame, text="", font=("Helvetica", 24, "bold"),
                    width=4, height=2, bd=2, relief="groove"
                )
                label.grid(row=i, column=j, padx=4, pady=4)
                self.tiles[i][j] = label

    def update_grid(self, state):
        for i in range(3):
            for j in range(3):
                val = state[i][j]
                if val == 0:
                    self.tiles[i][j].config(text="", bg="#34495e")
                else:
                    self.tiles[i][j].config(text=str(val), bg="#ecf0f1", fg="#2c3e50")

    def solve_puzzle(self):
        selection = self.heuristic_var.get()
        if "h1 (Misplaced)" in selection:
            heuristic = misplaced_tiles
        elif "h2 (Manhattan)" in selection:
            heuristic = manhattan_distance
        else:
            heuristic = combined_heuristic
            
        self.path, expanded = astar(start, heuristic)
        
        self.status_label.config(
            text=f"Nodes Expanded: {expanded} | Moves: {len(self.path)-1}"
        )
        
        self.solve_button.config(state="disabled", bg="#95a5a6")
        self.animation_idx = 0
        self.animate_solution()

    def animate_solution(self):
        if self.animation_idx < len(self.path):
            self.update_grid(self.path[self.animation_idx])
            self.animation_idx += 1
            self.root.after(600, self.animate_solution)
        else:
            self.solve_button.config(state="normal", bg="#2ecc71")

if __name__ == "__main__":
    root = tk.Tk()
    app = PuzzleGUI(root)
    root.mainloop()