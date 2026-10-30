
class ModelBasedAgent:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.position = start
        self.goal = goal
        self.visited = set()
        self.known_obstacles = set()
        self.path = [start]

    def navigate(self):
        while self.position != self.goal:
            self.visited.add(self.position)
            r, c = self.position
            neighbors = []

            for dr, dc, action in [
                (-1, 0, "UP"),
                (1, 0, "DOWN"),
                (0, -1, "LEFT"),
                (0, 1, "RIGHT"),
            ]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[0]):
                    if self.grid[nr][nc] == 1:
                        self.known_obstacles.add((nr, nc))
                    elif (nr, nc) not in self.visited:
                        neighbors.append(((nr, nc), action))

            if not neighbors:
                print("No valid path available.")
                return

            next_pos, action = min(
                neighbors,
                key=lambda x: abs(x[0][0] - self.goal[0])
                + abs(x[0][1] - self.goal[1]),
            )
            print(self.position, "->", action, "->", next_pos)
            self.position = next_pos
            self.path.append(next_pos)

        print("Goal reached!")
        print("Path:", self.path)
        print("Visited:", self.visited)
        print("Obstacles:", self.known_obstacles)


grid = [
    [0, 0, 0, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
]
agent = ModelBasedAgent(grid, (0, 0), (3, 3))
agent.navigate()