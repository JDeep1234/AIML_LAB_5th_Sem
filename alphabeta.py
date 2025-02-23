pruned_nodes = []  # Global list to store pruned nodes  

def minimax(node, depth, alpha, beta, maximizingPlayer):  
    global pruned_nodes  
    if depth == 0 or isinstance(node, int):  
        return node  

    if maximizingPlayer:  
        maxEva = float('-inf')  
        for child in node:  
            eva = minimax(child, depth - 1, alpha, beta, False)  
            maxEva = max(maxEva, eva)  
            alpha = max(alpha, maxEva)  
            if beta <= alpha:  
                pruned_nodes.append(eva)  # Append the pruned node  
                break  
        return maxEva  

    else:  
        minEva = float('inf')  
        for child in node:  
            eva = minimax(child, depth - 1, alpha, beta, True)  
            minEva = min(minEva, eva)  
            beta = min(beta, minEva)  
            if beta <= alpha:  
                pruned_nodes.append(eva)  # Append the pruned node  
                break  
        return minEva  

def build_tree(flat_tree, depth):  
    """Convert a flat array into a nested tree structure."""  
    if depth == 0:  
        return flat_tree.pop(0)  
    children = []  
    for _ in range(2):  
        children.append(build_tree(flat_tree, depth - 1))  
    return children  

# Input  
flattened_tree = list(map(int, input("Enter the flattened game tree (space-separated): ").split()))  
depth = int(input("Enter the depth of the tree: "))  

# Build the tree  
game_tree = build_tree(flattened_tree, depth)  

# Evaluate the tree and track pruned nodes  
evaluated_value = minimax(game_tree, depth, alpha=float('-inf'), beta=float('inf'), maximizingPlayer=True)  

# Output  
print("Evaluated Value:", evaluated_value)  
print("Pruned Nodes:", pruned_nodes)
