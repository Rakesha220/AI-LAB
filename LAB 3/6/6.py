
import math
import random

# Objective function to be minimized
def objective(x):
    return (x - 3) ** 2


# Generate a neighbouring state
def generate_neighbour(x):
    return x + random.uniform(-1, 1)


# Simulated Annealing Algorithm
def simulated_annealing(initial_state, initial_temperature,
                        cooling_rate, minimum_temperature,
                        maximum_iterations, seed):

    random.seed(seed)

    current_state = initial_state
    current_cost = objective(current_state)

    best_state = current_state
    best_cost = current_cost

    temperature = initial_temperature

    for iteration in range(maximum_iterations):

        if temperature <= minimum_temperature:
            break

        # Generate candidate state
        candidate_state = generate_neighbour(current_state)
        candidate_cost = objective(candidate_state)

        # Calculate change in cost
        delta = candidate_cost - current_cost

        # Accept or reject candidate
        if delta < 0:
            accept = True
        else:
            probability = math.exp(-delta / temperature)
            accept = random.random() < probability

        # Update current state
        if accept:
            current_state = candidate_state
            current_cost = candidate_cost

            # Update best state
            if current_cost < best_cost:
                best_state = current_state
                best_cost = current_cost

        # Reduce temperature
        temperature = temperature * cooling_rate

    return best_state, best_cost


# Main Program
print("SIMULATED ANNEALING ALGORITHM")
print("1. Initial State at the Optimum")
print("2. Initial State Below the Optimum")
print("3. Initial State Above the Optimum")
print("4. Low Initial Temperature")
print("5. Fast Cooling Schedule")

choice = int(input("Enter test case (1-5): "))


# Test Case 1
if choice == 1:
    initial_state = 3
    initial_temperature = 100
    cooling_rate = 0.95
    minimum_temperature = 0.01
    maximum_iterations = 500
    seed = 1

# Test Case 2
elif choice == 2:
    initial_state = -5
    initial_temperature = 100
    cooling_rate = 0.95
    minimum_temperature = 0.01
    maximum_iterations = 500
    seed = 42

# Test Case 3
elif choice == 3:
    initial_state = 9
    initial_temperature = 100
    cooling_rate = 0.95
    minimum_temperature = 0.01
    maximum_iterations = 500
    seed = 7

# Test Case 4
elif choice == 4:
    initial_state = 0
    initial_temperature = 1
    cooling_rate = 0.9
    minimum_temperature = 0.01
    maximum_iterations = 500
    seed = 10

# Test Case 5
elif choice == 5:
    initial_state = 10
    initial_temperature = 100
    cooling_rate = 0.5
    minimum_temperature = 0.01
    maximum_iterations = 100
    seed = 21

else:
    print("Invalid test case selection")
    exit()


# Execute the algorithm
best_state, best_cost = simulated_annealing(
    initial_state,
    initial_temperature,
    cooling_rate,
    minimum_temperature,
    maximum_iterations,
    seed
)

# Display results
print("\nBest State (x): {:.6f}".format(best_state))
print("Minimum Function Value: {:.8f}".format(best_cost))
