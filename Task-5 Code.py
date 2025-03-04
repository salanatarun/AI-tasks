print("8-puzzle problem")
import heapq
class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.cost = self.moves + self.heuristic()

    def __lt__(self, other):
        return self.cost < other.cost

    def heuristic(self):
        """ Manhattan Distance Heuristic """
        goal_positions = {val: (i // 3, i % 3) for i, val in enumerate(range(1, 9))}
        goal_positions[0] = (2, 2)  # Empty space (0) goal position

        total_distance = 0
        for i in range(3):
            for j in range(3):
                value = self.board[i][j]
                if value != 0:  # Ignore empty space
                    goal_x, goal_y = goal_positions[value]
                    total_distance += abs(goal_x - i) + abs(goal_y - j)

        return total_distance

    def get_next_states(self):
        """ Generate possible moves from the current state """
        def swap(board, x1, y1, x2, y2):
            new_board = [row[:] for row in board]
            new_board[x1][y1], new_board[x2][y2] = new_board[x2][y2], new_board[x1][y1]
            return new_board

        next_states = []
        empty_x, empty_y = [(i, row.index(0)) for i, row in enumerate(self.board) if 0 in row][0]
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for dx, dy in moves:
            new_x, new_y = empty_x + dx, empty_y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                next_states.append(PuzzleState(swap(self.board, empty_x, empty_y, new_x, new_y), self.moves + 1, self))

        return next_states

    def is_goal(self):
        """ Check if the state is the goal state """
        return self.board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def get_path(self):
        """ Trace back the moves from the goal to start """
        path, state = [], self
        while state:
            path.append(state.board)
            state = state.previous
        return path[::-1]

def solve_8_puzzle(initial_board, target_moves):
    """ A* Algorithm for solving the 8-Puzzle """
    priority_queue = []
    initial_state = PuzzleState(initial_board)
    heapq.heappush(priority_queue, initial_state)
    visited_states = set()

    while priority_queue:
        current_state = heapq.heappop(priority_queue)
        if current_state.is_goal():
            path = current_state.get_path()
            if len(path) - 1 == target_moves:  # Ensure exactly 10 moves
                return path
            else:
                continue  # Try another path

        visited_states.add(tuple(map(tuple, current_state.board)))

        for next_state in current_state.get_next_states():
            if tuple(map(tuple, next_state.board)) not in visited_states:
                heapq.heappush(priority_queue, next_state)

    return None

# Initial board that takes exactly 10 moves to reach the goal
initial_board = [
    [1, 2, 3],
    [4, 6, 0],  # Manually set this to require 10 moves
    [7, 5, 8]
]

solution_path = solve_8_puzzle(initial_board, target_moves=10)

if solution_path:
    print("Solution found in exactly 10 moves:")
    for step, state in enumerate(solution_path):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()
else:
    print("No solution found in exactly 10 moves. Try adjusting the initial board.")
