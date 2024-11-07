import itertools

# Function to solve SEND + MORE = MONEY using brute force
def solve_cryptarithmetic():
    # Define the letters involved in the puzzle
    letters = 'SENDMOREY'

    # Generate all possible permutations of digits (0-9)
    for perm in itertools.permutations(range(10), len(letters)):
        # Map each letter to a corresponding digit in the current permutation
        solution = dict(zip(letters, perm))

        # Ensure that 'S' and 'M' are non-zero since they are leading digits
        if solution['S'] == 0 or solution['M'] == 0:
            continue

        # Extract the numbers based on the current letter-digit mapping
        send = solution['S'] * 1000 + solution['E'] * 100 + solution['N'] * 10 + solution['D']
        more = solution['M'] * 1000 + solution['O'] * 100 + solution['R'] * 10 + solution['E']
        money = solution['M'] * 10000 + solution['O'] * 1000 + solution['N'] * 100 + solution['E'] * 10 + solution['Y']

        # Check if the equation SEND + MORE = MONEY holds
        if send + more == money:
            # If it does, return the solution
            return solution, send, more, money

# Solving the puzzle
solution, send, more, money = solve_cryptarithmetic()

# Output the solution
print("Solution:")
for letter, digit in solution.items():
    print(f"{letter} = {digit}")

print(f"\nSEND = {send}")
print(f"MORE = {more}")
print(f"MONEY = {money}")
