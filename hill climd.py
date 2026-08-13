# Hill Climbing Algorithm - 8 Puzzle

GOAL = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]


def print_board(board):
    for i in range(0, 9, 3):
        print(board[i:i + 3])
    print()


# Objective function
def objective(board):
    return sum(board[i] == GOAL[i] for i in range(9))


# Generate neighboring states
def get_neighbors(board):
    neighbors = []

    blank = board.index(0)
    row = blank // 3
    col = blank % 3

    moves = []

    if row > 0:
        moves.append(blank - 3)

    if row < 2:
        moves.append(blank + 3)

    if col > 0:
        moves.append(blank - 1)

    if col < 2:
        moves.append(blank + 1)

    for position in moves:
        new_board = board.copy()

        new_board[blank], new_board[position] = \
            new_board[position], new_board[blank]

        neighbors.append(new_board)

    return neighbors


def hill_climbing(start):
    current_state = start
    current_score = objective(current_state)

    print("Starting State:")
    print_board(current_state)
    print("Objective Value:", current_score)

    while True:

        # Check whether goal is reached
        if current_state == GOAL:
            print("Goal State Reached!")
            return

        neighbors = get_neighbors(current_state)

        best_state = current_state
        best_score = current_score

        # Find the best neighboring state
        for state in neighbors:
            score = objective(state)

            if score > best_score:
                best_state = state
                best_score = score

        # No improvement
        if best_score <= current_score:
            print("No better state found.")
            print("Hill Climbing stopped.")
            return

        # Set new current state
        current_state = best_state
        current_score = best_score

        print("New Current State:")
        print_board(current_state)
        print("Objective Value:", current_score)


# Initial state
initial_state = [
    1, 2, 3,
    4, 5, 6,
    0, 7, 8
]

hill_climbing(initial_state)

'''
OUTPUT
Starting State:
[1, 2, 3]
[4, 5, 6]
[0, 7, 8]

Objective Value: 6
New Current State:
[1, 2, 3]
[4, 5, 6]
[7, 0, 8]

Objective Value: 7
New Current State:
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]

Objective Value: 9
Goal State Reached!'''

