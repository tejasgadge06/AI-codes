 
def alpha_beta(node, depth, alpha, beta, maximizing_player): 
    if depth == 0 or not isinstance(node, list): 
        return node 
 
    if maximizing_player: 
        best_value = float('-inf') 
 
        for child in node: 
            value = alpha_beta(child, depth - 1, alpha, beta, False) 
            best_value = max(best_value, value) 
            alpha = max(alpha, best_value) 
 
            if alpha >= beta: 
                print("Pruning at MAX node") 
                break 
 
        return best_value 
 
    else: 
        best_value = float('inf') 
 
        for child in node: 
            value = alpha_beta(child, depth - 1, alpha, beta, True) 
            best_value = min(best_value, value) 
            beta = min(beta, best_value) 
 
            if alpha >= beta: 
                print("Pruning at MIN node") 
                break 
 
        return best_value 
 
# Game Tree 
game_tree = [ 
    [ 
        [3, 5], 
        [6, 9] 
    ], 
    [ 
        [1, 2], 
        [0, -1] 
    ] 
] 
# Initial values 
alpha = float('-inf') 
beta = float('inf') 
 
# Calculate optimal value 
result = alpha_beta( 
    game_tree, 
    3, 
    alpha, 
    beta, 
    True 
) 
print("\nOptimal value:", result)