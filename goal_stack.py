class BlockWorld:
    def __init__(self):
        self.state = {
            "on": {},  # Maps block to what it's on (another block or table)
            "clear": {},  # Maps block to whether it's clear (nothing on top)
            "holding": None,  # None if not holding any block, otherwise the block name
            "table": []  # List of blocks directly on the table
        }

    def initialize(self, blocks_on_table):
        """Initialize the block world with blocks on the table."""
        self.state["table"] = blocks_on_table[:]
        for block in blocks_on_table:
            self.state["on"][block] = "table"
            self.state["clear"][block] = True

    def move_to_table(self, block):
        """Move block to the table."""
        if self.state["on"][block] != "table":
            print(f"Action: Move {block} to the table")
            self.state["on"][block] = "table"
            self.state["table"].append(block)
            self.state["clear"][block] = True

    def move(self, block, destination):
        """Move block to the destination block."""
        print(f"Action: Move {block} onto {destination}")
        self.state["on"][block] = destination
        self.state["clear"][destination] = False

    def pop_stack(self, stack):
        return stack.pop() if stack else None

    def push_stack(self, stack, goal):
        stack.append(goal)

    def goal_stack_planning(self, goal_state):
        """Perform Goal Stack Planning to achieve the goal state from the current state."""
        stack = [goal_state]
        current_state = self.state.copy()  # Use the initial state set up earlier

        while stack:
            goal = self.pop_stack(stack)

            # If the goal is an action, perform it and modify the current state
            if isinstance(goal, tuple) and goal[0] == "move":
                block, destination = goal[1], goal[2]
                if current_state["on"][block] != destination:
                    # Move the block to its destination
                    if destination == "table":
                        self.move_to_table(block)
                    else:
                        self.move(block, destination)
                    # Update current state
                    current_state["on"][block] = destination
                    current_state["clear"][block] = True
                    if destination != "table":
                        current_state["clear"][destination] = False

            # If the goal is to satisfy a condition, break it down into sub-goals
            elif isinstance(goal, dict):
                for block, destination in goal.items():
                    # Check if block is in the correct place, if not, add necessary actions
                    if current_state["on"][block] != destination:
                        if destination == "table":
                            self.push_stack(stack, ("move", block, destination))
                        else:
                            # Ensure destination block is clear before moving the block
                            if not current_state["clear"][destination]:
                                self.push_stack(stack, ("move", destination, "table"))
                            self.push_stack(stack, ("move", block, destination))
                    else:
                        print(f"Goal: {block} is already on {destination}")

        print("Goal achieved!")

# Example run
if __name__ == "__main__":
    # Create an instance of the BlockWorld problem
    block_world = BlockWorld()

    # Initialize the block world (blocks A and B on the table)
    block_world.initialize(["A", "B"])

    # Define the goal state
    goal_state = {
        "A": "B",  # A should be on B
        "B": "table"  # B should be on the table
    }

    # Run the goal stack planner
    # TC:O(G*A*P)
    # SC:O(G+A) goal ,action ,precondition per action
    print("Initial State:", block_world.state)
    block_world.goal_stack_planning(goal_state)
    print("Final State:", block_world.state)
