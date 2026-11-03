
def hill_climbing(graph, values, initial_state):

    # Check whether initial state exists
    if initial_state not in graph:
        print("Invalid initial state")
        return

    # Set current state
    current = initial_state

    while True:

        # Assume current state is the best
        best_neighbour = current

        # Check all neighbouring states
        for neighbour in graph[current]:

            if values[neighbour] > values[best_neighbour]:
                best_neighbour = neighbour

        # Stop if no better neighbour exists
        if best_neighbour == current:
            break

        # Move to the best neighbour
        current = best_neighbour

    # Display final result
    print("Final State:", current)
    print("Evaluation Value:", values[current])


# Test Case Selection
print("HILL CLIMBING ALGORITHM")
print("1. Normal hill climbing")
print("2. Initial state is the best state")
print("3. Single neighbouring state")
print("4. Local maximum")
print("5. Plateau")
print("6. All neighbours have lower values")
print("7. Multiple neighbouring states")
print("8. Initial state has no neighbours")
print("9. Invalid initial state")
print("10. Local maximum versus global maximum")

choice = int(input("Enter test case (1-10): "))


# Test Case 1
if choice == 1:
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [], 'E': [], 'F': [], 'G': []
    }

    values = {
        'A': 2, 'B': 4, 'C': 5,
        'D': 7, 'E': 6, 'F': 8, 'G': 9
    }

    initial_state = 'A'


# Test Case 2
elif choice == 2:
    graph = {
        'A': ['B', 'C'],
        'B': [],
        'C': []
    }

    values = {'A': 10, 'B': 5, 'C': 7}
    initial_state = 'A'


# Test Case 3
elif choice == 3:
    graph = {
        'A': ['B'],
        'B': []
    }

    values = {'A': 3, 'B': 8}
    initial_state = 'A'


# Test Case 4
elif choice == 4:
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': [],
        'E': []
    }

    values = {'A': 3, 'B': 8, 'C': 5, 'D': 6, 'E': 10}
    initial_state = 'A'


# Test Case 5
elif choice == 5:
    graph = {
        'A': ['B', 'C'],
        'B': [],
        'C': []
    }

    values = {'A': 5, 'B': 5, 'C': 5}
    initial_state = 'A'


# Test Case 6
elif choice == 6:
    graph = {
        'A': ['B', 'C'],
        'B': [],
        'C': []
    }

    values = {'A': 9, 'B': 6, 'C': 4}
    initial_state = 'A'


# Test Case 7
elif choice == 7:
    graph = {
        'A': ['B', 'C', 'D'],
        'B': [],
        'C': [],
        'D': []
    }

    values = {'A': 2, 'B': 5, 'C': 9, 'D': 7}
    initial_state = 'A'


# Test Case 8
elif choice == 8:
    graph = {'A': []}
    values = {'A': 5}
    initial_state = 'A'


# Test Case 9
elif choice == 9:
    graph = {
        'A': ['B'],
        'B': []
    }

    values = {'A': 3, 'B': 8}
    initial_state = 'X'


# Test Case 10
elif choice == 10:
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': [],
        'E': []
    }

    values = {'A': 2, 'B': 8, 'C': 4, 'D': 6, 'E': 10}
    initial_state = 'A'


else:
    print("Invalid test case selection")
    exit()


# Execute Hill Climbing
print("\nInitial State:", initial_state)

hill_climbing(graph, values, initial_state)
