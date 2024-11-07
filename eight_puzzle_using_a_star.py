import heapq

# Function to find the index of the empty space (represented as 0)
def find_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Manhattan distance heuristic function
def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:  # Ignore the blank tile
                x, y = divmod(state[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

# Function to check if a state is the goal state
def is_goal(state, goal):
    return state == goal

# Function to generate possible moves from the current state
def generate_neighbors(state):
    neighbors = []
    i, j = find_blank_position(state)
    # Directions for moving the blank space (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            # Create a new state with the blank tile moved
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            neighbors.append(new_state)
    return neighbors

# Function to solve the 8-puzzle using A* algorithm
def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start, 0))  # (f, state, g)
    closed_list = set()
    came_from = {}  # To track the path

    while open_list:
        _, current_state, g = heapq.heappop(open_list)

        if is_goal(current_state, goal):
            return reconstruct_path(came_from, current_state)

        closed_list.add(tuple(map(tuple, current_state)))

        for neighbor in generate_neighbors(current_state):
            neighbor_tuple = tuple(map(tuple, neighbor))

            if neighbor_tuple in closed_list:
                continue

            tentative_g = g + 1
            h = manhattan_distance(neighbor, goal)
            f = tentative_g + h

            heapq.heappush(open_list, (f, neighbor, tentative_g))
            came_from[neighbor_tuple] = current_state

    return None  # Return None if no solution is found

# Function to reconstruct the path from the start to the goal
def reconstruct_path(came_from, current):
    path = [current]
    while tuple(map(tuple, current)) in came_from:
        current = came_from[tuple(map(tuple, current))]
        path.append(current)
    path.reverse()
    return path

# Function to print the puzzle state
def print_puzzle(state):
    for row in state:
        print(row)
    print()

# Main function
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

    print("Solving the 8-Puzzle using A* algorithm...\n")

    solution_path = a_star(start_state, goal_state)

    if solution_path:
        print(f"Solution found in {len(solution_path) - 1} moves:")
        for step in solution_path:
            print_puzzle(step)
    else:
        print("No solution found!")
# TC:O(branching_factor^depth) (TC=SC)
