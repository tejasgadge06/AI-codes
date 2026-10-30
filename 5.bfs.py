from collections import deque 
 
def bfs(grid, start, goal): 
    rows = len(grid) 
    cols = len(grid[0]) 
    queue = deque([start]) 
    visited = {start} 
    parent = {start: None} 
 
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
 
    while queue: 
        current = queue.popleft() 
 
        if current == goal: 
            path = [] 
            while current is not None: 
                path.append(current) 
                current = parent[current] 
            return path[::-1] 
 
        for dr, dc in directions: 
            r = current[0] + dr 
            c = current[1] + dc 
 
            if (0 <= r < rows and 0 <= c < cols and 
                    grid[r][c] != 1 and (r, c) not in visited): 
 
                visited.add((r, c)) 
                parent[(r, c)] = current 
                queue.append((r, c)) 
 
    return None 
 

grid = [ 
    [0, 0, 0, 1], 
    [1, 0, 0, 1], 
    [1, 0, 0, 0] 
] 
 
start = (0, 0) 
goal = (2, 3) 
 
path = bfs(grid, start, goal) 
 
if path: 
    print("Shortest Path:") 
    print(path) 
    print("Path Length:", len(path) - 1) 
else: 
    print("No path found")