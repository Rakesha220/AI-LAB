def vacuum_agent(location, status_a, status_b):
    """
    Determines the next action based on current location and status of rooms.
    Reflects the agent function from the pseudocode.
    """
    if location == 'A' and status_a == 'Dirty':
        return 'SUCK'
    elif location == 'B' and status_b == 'Dirty':
        return 'SUCK'
    elif status_a == 'Dirty':
        return 'LEFT'
    elif status_b == 'Dirty':
        return 'RIGHT'
    else:
        return 'NO-OP'


def vacuum_simulation(initial_location, status_a, status_b):
    """
    Simulates the vacuum cleaner agent until both rooms are clean.
    """
    location = initial_location
    
    print("\n--- Starting Vacuum Simulation ---")
    print(f"Initial State -> Location: {location}, Room A: {status_a}, Room B: {status_b}\n")
    
    step = 1
    while True:
        action = vacuum_agent(location, status_a, status_b)
        
        if action == 'NO-OP':
            print(f"Step {step}: Action = NO-OP (Both rooms are clean. Stopping simulation.)")
            break
            
        print(f"Step {step}: Action = {action}")
        
        # Update environment state
        if action == 'SUCK' and location == 'A':
            status_a = 'Clean'
        elif action == 'SUCK' and location == 'B':
            status_b = 'Clean'
        elif action == 'LEFT':
            location = 'A'
        elif action == 'RIGHT':
            location = 'B'
            
        print(f"        Current State -> Location: {location}, Room A: {status_a}, Room B: {status_b}")
        step += 1
        
    print("\n=== FINAL ENVIRONMENT STATE ===")
    print(f"Final Location: {location}")
    print(f"Room A Status:  {status_a}")
    print(f"Room B Status:  {status_b}")


def main():
    print("=== PROGRAM 4: VACUUM CLEANER AGENT ===")
    
    # Reading input from user
    location = input("Initial Location (A/B): ").strip().upper()
    status_a = input("Room A Status (Clean/Dirty): ").strip().capitalize()
    status_b = input("Room B Status (Clean/Dirty): ").strip().capitalize()
    
    vacuum_simulation(location, status_a, status_b)


if __name__ == "__main__":
    main()