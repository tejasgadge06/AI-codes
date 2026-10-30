 
import heapq 
def h(state, goal): 
    d = 0 
    for n in range(1, 9):
        a = state.index(n) 
        b = goal.index(n) 
 
        d += abs(a // 3 - b // 3) 
        d += abs(a % 3 - b % 3) 
    return d
 
def neighbors(state): 
    zero = state.index(0)
    r, c = zero // 3, zero % 3

    moves = [
        (-1, 0, "UP"),
        (1, 0, "DOWN"),
        (0, -1, "LEFT"),
        (0, 1, "RIGHT")
    ]

    result = []
    for dr, dc, move in moves:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            nz = nr * 3 + nc
            s = list(state)
            s[zero], s[nz] = s[nz], s[zero]
            result.append((tuple(s), move))
    return result
 
def show(state): 
    for i in range(0, 9, 3): 
        print(state[i:i+3]) 
    print() 
 
def a_star(start, goal): 
    pq = [(h(start, goal), 0, start, [])] 
    visited = set() 
    while pq: 
        f, g, state, path = heapq.heappop(pq) 
        if state in visited: 
            continue 
        visited.add(state) 
        if state == goal: 
            print("Solution found!") 
            print("Moves:", len(path)) 
            print("Solution Path:\n") 
            show(start) 
            for move, s in path: 
                print("Move:", move) 
                show(s) 
            return 
        for next_state, move in neighbors(state): 
            if next_state not in visited: 
                ng = g + 1 
                heapq.heappush( 
                    pq, 
                    ( 
                        ng + h(next_state, goal), 
                        ng, 
                        next_state, 
                        path + [(move, next_state)] 
                    ) 
                ) 
 
    print("No solution found.") 
start = ( 
    1, 2, 3, 
    4, 0, 6, 
    7, 5, 8 
) 
goal = ( 
    1, 2, 3, 
    4, 5, 6, 
    7, 8, 0 
)
a_star(start, goal)