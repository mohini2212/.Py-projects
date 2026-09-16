def create_board(n):
    """Create an N x N board filled with 0s."""
    return [[0 for _ in range(n)] for _ in range(n)]

def print_board(board):
    """Print the board in a readable format."""
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()

def is_safe(board, row, col, n):
    """Check if placing a queen at (row, col) is safe."""

    # Check the same column (all rows above)
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n, solutions):
    """Use backtracking to place queens row by row."""

    # Base case: all queens placed successfully
    if row == n:
        # Save a copy of this solution
        solution_copy = [r[:] for r in board]
        solutions.append(solution_copy)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1          # place queen
            solve_n_queens(board, row + 1, n, solutions)  # recurse
            board[row][col] = 0          # backtrack (remove queen)

def main():
    n = int(input("Enter the value of N: "))

    board = create_board(n)
    solutions = []

    solve_n_queens(board, 0, n, solutions)

    print(f"\nTotal solutions found: {len(solutions)}\n")

    if solutions:
        show = input("Do you want to print all solutions? (y/n): ")
        if show.lower() == "y":
            for idx, sol in enumerate(solutions, start=1):
                print(f"Solution {idx}:")
                print_board(sol)
    else:
        print("No solution exists for this N.")

if __name__ == "__main__":
    main()