import time

N = 8  # Board size (8x8)

def print_solution(board, method, step=None):
    """Prints the chessboard solution."""
    if step is not None:
        print(f"\nStep {step}: Placing queen {step} using {method}")
    else:
        print(f"\nFinal Solution using {method}:")

    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")
    time.sleep(1)  # Delay for visualization


def is_safe(board, row, col):
    """Checks if a queen can be placed at board[row][col]."""
    for i in range(row):  
        if board[i][col]: return False  # Check column
        if col - (row - i) >= 0 and board[i][col - (row - i)]: return False  # Check left diagonal
        if col + (row - i) < N and board[i][col + (row - i)]: return False  # Check right diagonal
    return True


def solve_all_at_once(board, row):
    """Method 1: Place all 8 queens at once using backtracking."""
    if row >= N:  # If all queens are placed
        print_solution(board, "Method 1 (All at Once)")
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            if solve_all_at_once(board, row + 1):  # Recur for next queen
                return True
            board[row][col] = 0  # Backtrack

    return False  # No valid position for this row


def solve_one_by_one(board, row, step=1):
    """Method 2: Place queens one by one with visualization."""
    if row == N:  # If all queens are placed
        print_solution(board, "Method 2 (One by One)")
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            print_solution(board, "Method 2 (One by One)", step)  # Show step-by-step placement
            if solve_one_by_one(board, row + 1, step + 1):  # Recur for next queen
                return True
            board[row][col] = 0  # Backtrack

    return False  # If no column works, backtrack


def main():
    """Runs both methods automatically."""
    board1 = [[0] * N for _ in range(N)]  # Initialize empty board for Method 1
    board2 = [[0] * N for _ in range(N)]  # Initialize empty board for Method 2

    # Run Method 1 (All at Once)
    solve_all_at_once(board1, 0)

    # Run Method 2 (One by One with steps)
    solve_one_by_one(board2, 0)


if __name__ == "__main__":
    main()
