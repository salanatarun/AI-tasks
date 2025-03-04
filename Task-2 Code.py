print("Task-2 Water Jug Problem")
def is_valid_state(state, visited):

    return state not in visited

def water_jug_problem():
    # Jug capacities
    max_a = 3
    max_b = 5
    goal = 4

    # Initial state
    initial_state = (0, 0)
    visited = set()
    stack = [(initial_state, [])]

    while stack:
        (a, b), path = stack.pop()


        if a == goal or b == goal:
            return path + [(a, b)]
        visited.add((a, b))
        next_states = [
            (max_a, b),  # Fill Jug A
            (a, max_b),  # Fill Jug B
            (0, b),      # Empty Jug A
            (a, 0),      # Empty Jug B
            (a - min(a, max_b - b), b + min(a, max_b - b)),  # Pour A -> B
            (a + min(b, max_a - a), b - min(b, max_a - a))   # Pour B -> A
        ]

        # Add valid next states to the stack
        for state in next_states:
            if is_valid_state(state, visited):
                stack.append((state, path + [(a, b)]))

    return None

solution = water_jug_problem()
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
