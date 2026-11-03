
import heapq

def a_star(graph, heuristic, start, goal):

    # Check whether start and goal nodes exist
    if start not in graph:
        print("Invalid start node")
        return

    if goal not in graph:
        print("Goal node does not exist")
        return

    # Initialize priority queue
    OPEN = []
    heapq.heappush(OPEN, (heuristic[start], start))

    # Initialize costs and parent
    g = {start: 0}
    parent = {start: None}

    while OPEN:

        # Remove node with lowest f value
        f_current, current = heapq.heappop(OPEN)

        # Skip outdated queue entries
        if f_current != g[current] + heuristic[current]:
            continue

        # Check whether goal is reached
        if current == goal:

            # Reconstruct path
            path = []
            node = goal

            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()

            print("Optimal Path:", " -> ".join(path))
            print("Total Cost:", g[goal])
            return

        # Explore neighbouring nodes
        for neighbour, cost in graph[current].items():

            tentative_g = g[current] + cost

            # Update if a better path is found
            if neighbour not in g or tentative_g < g[neighbour]:

                g[neighbour] = tentative_g
                parent[neighbour] = current

                f = tentative_g + heuristic[neighbour]

                heapq.heappush(OPEN, (f, neighbour))

    print("No path exists")


# Base Graph
graph = {
    'A': {'B': 1, 'C': 2, 'H': 7},
    'B': {'D': 4, 'E': 6},
    'C': {'F': 3, 'G': 2},
    'D': {'E': 7},
    'E': {},
    'F': {'H': 1},
    'G': {'H': 2},
    'H': {}
}

# Heuristic Values
heuristic = {
    'A': 5, 'B': 3, 'C': 4, 'D': 2,
    'E': 6, 'F': 3, 'G': 1, 'H': 0
}


# Test Case Selection
print("A* SEARCH ALGORITHM")
print("1. Optimal path")
print("2. Start node is goal node")
print("3. Intermediate goal node")
print("4. Path through another branch")
print("5. Goal node does not exist")
print("6. Goal node is disconnected")
print("7. Direct path versus alternative path")
print("8. Invalid start node")

choice = int(input("Enter test case (1-8): "))

if choice == 1 or choice == 7:
    start, goal = 'A', 'H'

elif choice == 2:
    start, goal = 'A', 'A'

elif choice == 3:
    start, goal = 'A', 'D'

elif choice == 4:
    start, goal = 'A', 'F'

elif choice == 5:
    start, goal = 'A', 'Z'

elif choice == 6:
    graph = {
        'A': {'B': 2},
        'B': {'A': 2},
        'C': {}
    }

    heuristic = {
        'A': 2,
        'B': 1,
        'C': 0
    }

    start, goal = 'A', 'C'

elif choice == 8:
    start, goal = 'X', 'H'

else:
    print("Invalid test case selection")
    exit()

print("\nStart Node:", start)
print("Goal Node:", goal)

a_star(graph, heuristic, start, goal)
