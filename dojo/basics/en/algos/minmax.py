import math

# Constants for representing players and empty cells
EMPTY = "-"
PLAYER_X = "X"
PLAYER_O = "O"

def evaluate(board):
    """
    Evaluate the current state of the board.
    Return +1 if the computer wins, -1 if the player wins, or 0 for a tie.
    """
    # List of all possible winning combinations
    winning_combinations = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]

    # Check for a win
    for combo in winning_combinations:
        if combo == [PLAYER_X, PLAYER_X, PLAYER_X]:
            return 1  # Computer wins
        elif combo == [PLAYER_O, PLAYER_O, PLAYER_O]:
            return -1  # Player wins

    # No winner, it's a tie
    return 0

def minmax(board, depth, is_maximizing):
    """
    MinMax algorithm implementation.
    """
    score = evaluate(board)

    # Base cases
    if score == 1:
        return score - depth
    if score == -1:
        return score + depth
    if EMPTY not in board:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(len(board)):
            if board[i] == EMPTY:
                board[i] = PLAYER_X
                score = minmax(board, depth + 1, False)
                board[i] = EMPTY
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(len(board)):
            if board[i] == EMPTY:
                board[i] = PLAYER_O
                score = minmax(board, depth + 1, True)
                board[i] = EMPTY
                best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    """
    Get the best move for the computer using the MinMax algorithm.
    """
    best_score = -math.inf
    best_move = None
    for i in range(len(board)):
        if board[i] == EMPTY:
            board[i] = PLAYER_X
            score = minmax(board, 0, False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Example usage
board = [EMPTY, EMPTY, EMPTY,
         EMPTY, EMPTY, EMPTY,
         EMPTY, EMPTY, EMPTY]

# Computer's turn (player X)
best_move = get_best_move(board)
board[best_move] = PLAYER_X

# Print the updated board
print(board)
