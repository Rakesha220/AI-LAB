def depth_limited_search(node, goal, graph, limit, path):
    """
    Performs Depth-Limited Search recursively.
    Returns:
        - List representing path if goal is found
        - 'CUTOFF' if depth limit was reached
        - 'FAILURE' if goal is not found in this branch
    """
    if node == goal:
        return path + [node]
    
    if limit == 0:
        return "CUTOFF"
    
    cutoff_occurred = False
    
    for child in graph.get(node, []):
        if child not in path:
            result = depth_limited_search(child, goal, graph, limit - 1, path + [node])
            
            if result != "FAILURE" and result != "CUTOFF":
                return result  # Solution path found
            
            if result == "CUTOFF":
                cutoff_occurred = True
                
    if cutoff_occurred:
        return "CUTOFF"
    else:
        return "FAILURE"


def iterative_deepening_search(initial, goal, graph, maximum_depth):
    """
    Iterative Deepening Search (IDS) wrapper.
    Iterates depth limit from 0 up to maximum_depth.
    """
    for depth in range(maximum_depth + 1):
        result = depth_limited_search(initial, goal, graph, depth, [])
        
        if result != "CUTOFF" and result != "FAILURE":
            return result, depth  # Returns (path, depth)
            
    return None, None  # Goal not found within maximum depth


def parse_search_tree_input():
    """
    Reads search tree edges until an empty line is entered.
    Expected line formats:
        A: B, C
        B: -
    """
    graph = {}
    print("Enter the Search Tree (one line per node, e.g., 'A: B, C' or 'B: -').")
    print("Press Enter on an empty line when finished:")
    
    while True:
        line = input().strip()
        if not line:
            break
        
        if ":" in line:
            parent, children_str = line.split(":", 1)
            parent = parent.strip()
            children_str = children_str.strip()
            
            if children_str == "-" or not children_str:
                graph[parent] = []
            else:
                children = [c.strip() for c in children_str.split(",")]
                graph[parent] = children
                
    return graph


def main():
    print("=== PROGRAM 3: ITERATIVE DEEPENING SEARCH (IDS) ===\n")
    
    # 1. Read Inputs
    initial_state = input("Initial State: ").strip()
    goal_state = input("Goal State: ").strip()
    maximum_depth = int(input("Maximum Depth: ").strip())
    
    # 2. Read Search Tree
    graph = parse_search_tree_input()
    
    # 3. Perform Iterative Deepening Search
    path, found_depth = iterative_deepening_search(
        initial_state, goal_state, graph, maximum_depth
    )
    
    # 4. Display Results
    print("\n=== RESULT ===")
    if path:
        print(f"Goal '{goal_state}' found!")
        print(f"Solution Path: {' -> '.join(path)}")
        print(f"Depth Found: {found_depth}")
    else:
        print(f"Goal '{goal_state}' was NOT found within the maximum depth of {maximum_depth}.")


if __name__ == "__main__":
    main()