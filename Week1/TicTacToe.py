WINNING_LINES = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),
    (3, 5, 7),
)


def winner(board):
    """Return the winner, or None when the game has no winner yet."""
    for first, second, third in WINNING_LINES:
        if board[first] == board[second] == board[third] != " ":
            return board[first]
    return None


def get_all_solutions(board, player="X", moves=()):
    """Return every legal game completion from the current board."""
    game_winner = winner(board)
    empty_cells = [cell for cell in range(1, 10) if board[cell] == " "]

    if game_winner or not empty_cells:
        return [(moves, game_winner or "Draw", board.copy())]

    solutions = []
    for cell in empty_cells:
        next_board = board.copy()
        next_board[cell] = player
        solutions.extend(
            get_all_solutions(
                next_board,
                "O" if player == "X" else "X",
                moves + ((player, cell),),
            )
        )
    return solutions

print("USN: 1BM25CS489")
print("NAME: OMKAR SADASHIV KOKATNOOR");
print("")


def print_board(board):
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("---+---+---")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---+---+---")
    print(f" {board[7]} | {board[8]} | {board[9]} ")


board = [" "] * 10
for cell in (3, 4, 7):
    board[cell] = "X"
for cell in (1, 8, 9):
    board[cell] = "O"

solutions = get_all_solutions(board)
print(f"Number of possible solutions: {len(solutions)}")

for solution_number, (moves, result, final_board) in enumerate(solutions, 1):
    move_text = ", ".join(f"{player}{cell}" for player, cell in moves)
    print(f"\nSolution {solution_number}: {move_text} -> {result}")
    print_board(final_board)