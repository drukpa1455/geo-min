import numpy as np  # Importing the NumPy library

# Tree Structure
# ------------------------------------------
tree = {
    'A': np.array(['B', 'C']),  # Node A has children B and C
    'B': np.array(['D', 'E']),  # Node B has children D and E
    'C': np.array(['F', 'G']),  # Node C has children F and G
    'D': np.array(['H', 'I']),  # Node D has children H and I
    'E': np.array([]),  # Node E has no children
    'F': np.array([]),  # Node F has no children
    'G': np.array([]),  # Node G has no children
    'H': np.array([]),  # Node H has no children
    'I': np.array([])   # Node I has no children
}

# Depth-First Search (DFS)
# ------------------------------------------
def dfs(node):
    """
    Performs Depth-First Search (DFS) on the tree starting from the given node.

    Args:
        node (str): The starting node for DFS.

    Returns:
        None
    """
    if node is None:
        return  # Exit the current recursion if the node is None
    print("Visited node:", node)  # Print the current node being visited
    children = tree.get(node, np.array([]))  # Get the children of the current node from the tree dictionary
    for child in children:
        dfs(child)


# Breadth-First Search (BFS)
# ------------------------------------------
def bfs(root):
    """
    Performs Breadth-First Search (BFS) on the tree starting from the given root node.

    Args:
        root (str): The root node for BFS.

    Returns:
        None
    """
    queue = [root]  # Initialize a queue with the root node

    while queue:
        node = queue.pop(0)  # Get the node from the front of the queue
        print("Visited node:", node)  # Print the visited node

        children = tree.get(node, np.array([]))  # Get the children of the current node
        queue.extend(children)  # Add the children to the end of the queue for exploration


# Uniform Cost Search (UCS)
# ------------------------------------------
def ucs(root):
    """
    Performs Uniform Cost Search (UCS) on the tree starting from the given root node.

    Args:
        root (str): The root node for UCS.

    Returns:
        None
    """
    queue = [(0, root)]  # Initialize a priority queue with the root node and its cost
    while queue:
        cost, node = queue.pop(0)  # Get the node with the minimum cost from the front of the queue
        print("Visited node:", node)  # Print the visited node
        children = tree.get(node, np.array([]))  # Get the children of the current node
        queue.extend([(cost + 1, child) for child in children])  # Add the children to the queue with updated costs


# Iterative Deepening Depth-First Search (IDDFS)
# ------------------------------------------
def iddfs(root, depth_limit):
    """
    Performs Iterative Deepening Depth-First Search (IDDFS) on the tree starting from the given root node.

    Args:
        root (str): The root node for IDDFS.
        depth_limit (int): The maximum depth to explore.

    Returns:
        None
    """
    for depth in range(depth_limit + 1):  # Iterate over the depth limits from 0 to the specified depth limit
        if dfs_limit(root, depth):  # Call a helper function to perform DFS with a depth limit
            return

def dfs_limit(node, depth):
    """
    Helper function for IDDFS that performs DFS with a depth limit.

    Args:
        node (str): The current node.
        depth (int): The remaining depth limit.

    Returns:
        bool: True if the goal node is found within the depth limit, False otherwise.
    """
    if depth == 0:  # If the depth limit is reached
        print("Visited node:", node)  # Print the visited node
        return True
    children = tree.get(node, np.array([]))  # Get the children of the current node
    for child in children:
        if dfs_limit(child, depth - 1):  # Recursively call the helper function with the child node and reduced depth limit
            return True
    return False


# A* Search
# ------------------------------------------
def astar(root, heuristic):
    """
    Performs A* Search on the tree starting from the given root node using the specified heuristic function.

    Args:
        root (str): The root node for A* Search.
        heuristic (dict): The heuristic function that estimates the cost from each node to the goal node.

    Returns:
        None
    """
    open_list = [(heuristic[root], 0, root)]  # Initialize a priority queue with the root node, its cost, and heuristic value
    closed_list = set()  # Initialize a set to store visited nodes
    while open_list:
        _, cost, node = min(open_list)  # Get the node with the minimum combined cost and heuristic value
        open_list.remove((heuristic[node], cost, node))  # Remove the node from the open list
        closed_list.add(node)  # Add the node to the closed list
        print("Visited node:", node)  # Print the visited node
        if node == goal:  # If the goal node is found
            return
        children = tree.get(node, np.array([]))  # Get the children of the current node
        for child in children:
            if child not in closed_list:  # If the child node has not been visited
                g = cost + 1  # Increment the cost by 1
                h = heuristic[child]  # Get the heuristic value for the child node
                f = g + h  # Calculate the combined cost and heuristic value
                open_list.append((f, g, child))  # Add the child node to the open list with the updated values

# Best-First Search
# ------------------------------------------
def best_first(root, heuristic):
    """
    Performs Best-First Search on the tree starting from the given root node using the specified heuristic function.

    Args:
        root (str): The root node for Best-First Search.
        heuristic (dict): The heuristic function that estimates the desirability of each node.

    Returns:
        None
    """
    open_list = [(heuristic[root], root)]  # Initialize a priority queue with the root node and its heuristic value
    closed_list = set()  # Initialize a set to store visited nodes
    while open_list:
        _, node = min(open_list)  # Get the node with the minimum heuristic value
        open_list.remove((heuristic[node], node))  # Remove the node from the open list
        closed_list.add(node)  # Add the node to the closed list
        print("Visited node:", node)  # Print the visited node
        if node == goal:  # If the goal node is found
            return
        children = tree.get(node, np.array([]))  # Get the children of the current node
        for child in children:
            if child not in closed_list:  # If the child node has not been visited
                open_list.append((heuristic[child], child))  # Add the child node to the open list

# Greedy Search
# ------------------------------------------
def greedy(root, heuristic):
    """
    Performs Greedy Search on the tree starting from the given root node using the specified heuristic function.

    Args:
        root (str): The root node for Greedy Search.
        heuristic (dict): The heuristic function that estimates the desirability of each node.

    Returns:
        None
    """
    queue = [(heuristic[root], root)]  # Initialize a priority queue with the root node and its heuristic value
    while queue:
        _, node = min(queue)  # Get the node with the minimum heuristic value
        queue.remove((heuristic[node], node))  # Remove the node from the queue
        print("Visited node:", node)  # Print the visited node
        if node == goal:  # If the goal node is found
            return
        children = tree.get(node, np.array([]))  # Get the children of the current node
        queue.extend([(heuristic[child], child) for child in children])  # Add the children to the queue


# Minimax
# ------------------------------------------
class MinimaxNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def minimax(node, maximizing_player):
    """
    Performs the Minimax algorithm on the tree starting from the given node.

    Args:
        node (MinimaxNode): The current node.
        maximizing_player (bool): True if the current player is maximizing, False otherwise.

    Returns:
        int: The optimal value.
    """
    if len(node.children) == 0:  # If the current node is a leaf node
        return node.value
    if maximizing_player:  # If the current player is maximizing
        max_value = -np.inf
        for child in node.children:
            value = minimax(child, False)  # Recursively call the algorithm with the child node and set maximizing player to False
            max_value = max(max_value, value)  # Update the maximum value
        return max_value
    else:  # If the current player is minimizing
        min_value = np.inf
        for child in node.children:
            value = minimax(child, True)  # Recursively call the algorithm with the child node and set maximizing player to True
            min_value = min(min_value, value)  # Update the minimum value
        return min_value

def build_minimax_tree():
    """
    Builds a sample tree for Minimax algorithm.

    Returns:
        MinimaxNode: The root node of the tree.
    """
    root = MinimaxNode(3)
    child1 = MinimaxNode(5)
    child2 = MinimaxNode(2)
    child3 = MinimaxNode(9)
    child4 = MinimaxNode(8)
    child5 = MinimaxNode(1)
    root.children = [child1, child2]
    child1.children = [child3, child4]
    child2.children = [child5]
    return root


# Alpha-Beta Pruning
# ------------------------------------------
class AlphaBetaNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def alphabeta(node, alpha, beta, maximizing_player):
    """
    Performs the Alpha-Beta Pruning algorithm on the tree starting from the given node.

    Args:
        node (AlphaBetaNode): The current node.
        alpha (float): The current alpha value.
        beta (float): The current beta value.
        maximizing_player (bool): True if the current player is maximizing, False otherwise.

    Returns:
        int: The optimal value.
    """
    if len(node.children) == 0:  # If the current node is a leaf node
        return node.value
    if maximizing_player:  # If the current player is maximizing
        value = -np.inf
        for child in node.children:
            value = max(value, alphabeta(child, alpha, beta, False))  # Recursively call the algorithm with the child node and set maximizing player to False
            alpha = max(alpha, value)  # Update the alpha value
            if alpha >= beta:  # Perform alpha-beta pruning
                break
        return value
    else:  # If the current player is minimizing
        value = np.inf
        for child in node.children:
            value = min(value, alphabeta(child, alpha, beta, True))  # Recursively call the algorithm with the child node and set maximizing player to True
            beta = min(beta, value)  # Update the beta value
            if beta <= alpha:  # Perform alpha-beta pruning
                break
        return value

def build_alphabeta_tree():
    """
    Builds a sample tree for Alpha-Beta Pruning algorithm.

    Returns:
        AlphaBetaNode: The root node of the tree.
    """
    root = AlphaBetaNode(3)
    child1 = AlphaBetaNode(5)
    child2 = AlphaBetaNode(2)
    child3 = AlphaBetaNode(9)
    child4 = AlphaBetaNode(8)
    child5 = AlphaBetaNode(1)
    root.children = [child1, child2]
    child1.children = [child3, child4]
    child2.children = [child5]
    return root


# Monte Carlo Tree Search (MCTS)
# ------------------------------------------
class MCTSTreeNode:
    def __init__(self, name, wins, visits):
        self.name = name  # Unique identifier for the node
        self.wins = wins  # Number of wins recorded at this node
        self.visits = visits  # Number of visits to this node
        self.children = []  # List of child nodes

    def select_child_ucb(self, exploration_constant):
        """
        Selects the child node using the Upper Confidence Bound (UCB) formula.

        Args:
            exploration_constant (float): The exploration constant for UCB.

        Returns:
            MCTSTreeNode: The selected child node.
        """
        ucb_values = [
            child.wins / child.visits + exploration_constant * np.sqrt(np.log(self.visits) / child.visits)
            for child in self.children  # Compute UCB values for all children nodes
        ]
        max_index = np.argmax(ucb_values) # Find the child node with the maximum UCB value
        return self.children[max_index]  # Return the selected child node

    def expand(self):
        """
        Expands the current node by adding its child nodes.

        Returns:
            None
        """
        if self.name == 'A':
            self.children.append(MCTSTreeNode('B', 0, 0))
            self.children.append(MCTSTreeNode('C', 0, 0))
        elif self.name == 'B':
            self.children.append(MCTSTreeNode('D', 0, 0))
            self.children.append(MCTSTreeNode('E', 0, 0))
        elif self.name == 'C':
            self.children.append(MCTSTreeNode('F', 0, 0))
            self.children.append(MCTSTreeNode('G', 0, 0))
        elif self.name == 'D':
            self.children.append(MCTSTreeNode('H', 0, 0))
            self.children.append(MCTSTreeNode('I', 0, 0))
        elif self.name == 'E' or self.name == 'F' or self.name == 'G' or self.name == 'H' or self.name == 'I':
            pass

    def simulate(self):
        """
        Simulates a game play or outcome for the current node.

        Returns:
            int: The result of the simulation.
        """
        if self.name == 'I':
            return 1  # Return 1 (win) if the node's name is 'I
        return 0  # Return 0 (loss) otherwise

    def update(self, result):
        """
        Updates the wins and visits count for the current node.

        Args:
            result (int): The result of the simulation.

        Returns:
            None
        """
        self.visits += 1
        self.wins += result

def mcts(root, num_simulations):
    """
    Performs the Monte Carlo Tree Search (MCTS) algorithm on the tree starting from the given root node.

    Args:
        root (MCTSTreeNode): The root node for MCTS.
        num_simulations (int): The number of simulations to run.

    Returns:
        None
    """
    for _ in range(num_simulations):
        node = root  # Traverse down the tree until reaching a leaf node
        while node.children:
            node = node.select_child_ucb(1.4)
        if node.visits > 0:  # If the node has been visited before, expand and simulate it
            node.expand()
            result = node.simulate()
            node.update(result)

def build_mcts_tree():
    """
    Builds a sample tree for Monte Carlo Tree Search (MCTS) algorithm.

    Returns:
        MCTSTreeNode: The root node of the tree.
    """
    root = MCTSTreeNode('A', 0, 0)  # Create the root node
    return root  # Return the root of the tree


# Example usage
# ------------------------------------------
root = 'A'  # The starting node
goal = 'I'  # The goal node

print("Depth-First Search (DFS):")
dfs(root)  # Perform DFS starting from the root node

print("\nBreadth-First Search (BFS):")
bfs(root)  # Perform BFS starting from the root node

print("\nUniform Cost Search (UCS):")
ucs(root)  # Perform UCS starting from the root node

print("\nIterative Deepening Depth-First Search (IDDFS):")
iddfs(root, 3)  # Perform IDDFS starting from the root node with a depth limit of 3

print("\nA* Search:")
heuristic = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 3,
    'G': 4,
    'H': 1,
    'I': 0
}  # Heuristic function that estimates the cost from each node to the goal node
astar(root, heuristic)  # Perform A* Search starting from the root node with the specified heuristic function

print("\nBest-First Search:")
best_first(root, heuristic)  # Perform Best-First Search starting from the root node with the specified heuristic function

print("\nGreedy Search:")
greedy(root, heuristic)  # Perform Greedy Search starting from the root node with the specified heuristic function

print("\nMinimax:")
minimax_tree = build_minimax_tree()  # Build a sample tree for Minimax algorithm
result = minimax(minimax_tree, True)  # Perform Minimax starting from the root node with maximizing player set to True
print("Optimal value:", result)  # Print the optimal value determined by Minimax algorithm

print("\nAlpha-Beta Pruning:")
alphabeta_tree = build_alphabeta_tree()  # Build a sample tree for Alpha-Beta Pruning algorithm
result = alphabeta(alphabeta_tree, -np.inf, np.inf, True)  # Perform Alpha-Beta Pruning starting from the root node with initial alpha and beta values
print("Optimal value:", result)  # Print the optimal value determined by Alpha-Beta Pruning algorithm

print("\nMonte Carlo Tree Search (MCTS):")
mcts_tree = build_mcts_tree()  # Build a sample tree for Monte Carlo Tree Search algorithm
mcts(mcts_tree, 1000)  # Perform MCTS starting from the root node with 1000 simulations
best_child = max(mcts_tree.children, key=lambda child: child.visits)  # Select the child node with the maximum visits
print("Best child node:", best_child.name)  # Print the name of the best child node according to MCTS
