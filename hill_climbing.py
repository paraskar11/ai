import random

# Function to find the position of the blank tile (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Function to calculate Manhattan Distance (heuristic)
def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:  # Ignore the blank space
                x, y = divmod(state[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

# Generate all possible neighbors of the current state
def generate_neighbors(state):
    neighbors = []
    i, j = find_blank(state)
    # Define possible moves: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            neighbors.append(new_state)
    return neighbors

# Hill Climbing algorithm
def hill_climbing(start, goal):
    current_state = start
    current_cost = manhattan_distance(current_state, goal)
    
    while True:
        neighbors = generate_neighbors(current_state)
        next_state = None
        next_cost = current_cost
        
        # Evaluate each neighbor and choose the best one
        for neighbor in neighbors:
            cost = manhattan_distance(neighbor, goal)
            if cost < next_cost:
                next_state = neighbor
                next_cost = cost
        
        # If no better neighbor is found, return the current state
        if next_cost >= current_cost:
            return current_state, current_cost
        
        current_state = next_state
        current_cost = next_cost

# Function to print the puzzle state
def print_puzzle(state):
    for row in state:
        print(row)
    print()

# Main function to run the Hill Climbing algorithm
if __name__ == "__main__":
    # Initial state (can be customized)
    start_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    # Goal state
    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    print("Initial State:")
    print_puzzle(start_state)

    print("Running Hill Climbing algorithm...\n")

    final_state, final_cost = hill_climbing(start_state, goal_state)

    print("Final State (after Hill Climbing):")
    print_puzzle(final_state)
    print(f"Manhattan Distance Heuristic (Cost): {final_cost}")

    if final_state == goal_state:
        print("Solution found!")
    else:
        print("Hill Climbing stopped, no better state found (local maxima).")

# TC:O(moves)
# SC:O(1)
