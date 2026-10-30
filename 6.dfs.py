 
def dfs(cap_a, cap_b, goal): 
    stack = [(0, 0)] 
    visited = set() 
    parent = {(0, 0): None} 
 
    while stack: 
        state = stack.pop() 
 
        if state in visited: 
            continue 
 
        visited.add(state) 
        a, b = state 
 
        if a == goal or b == goal: 
            path = [] 
            while state is not None: 
                path.append(state) 
                state = parent[state] 
            return path[::-1] 
 
        next_states = [] 
 
        # Fill Jug A 
        next_states.append((cap_a, b)) 
 
        # Fill Jug B 
        next_states.append((a, cap_b)) 
 
        # Empty Jug A 
        next_states.append((0, b)) 
 
        # Empty Jug B 
        next_states.append((a, 0)) 
 
        # Pour A into B 
        amount = min(a, cap_b - b) 
        next_states.append((a - amount, b + amount)) 
 
        # Pour B into A 
        amount = min(b, cap_a - a) 
        next_states.append((a + amount, b - amount)) 
 
        for next_state in next_states: 
            if next_state not in visited: 
                parent[next_state] = (a, b) 
                stack.append(next_state) 
 
    return None 
 
 
# Jug capacities 
cap_a = 4 
cap_b = 3 
 
# Required amount 
goal = 2 
 
solution = dfs(cap_a, cap_b, goal) 
 
if solution: 
    print("Solution Path:") 
    for state in solution: 
        print(state) 
else: 
    print("No solution found")