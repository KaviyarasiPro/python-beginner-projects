def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


board = [str(i) for i in range(1, 10)]

winning_combinations = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]

for turn in range(9):
    display_board(board)

    player = "X" if turn % 2 == 0 else "O"

    while True:
        try:
            position = int(input(
                f"Player {player}, choose a position (1-9): "
            ))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if position < 1 or position > 9:
            print("Choose a position between 1 and 9!")
        elif board[position - 1] in ["X", "O"]:
            print("That position is already occupied!")
        else:
            board[position - 1] = player
            break

    if any(
        all(board[index] == player for index in combination)
        for combination in winning_combinations
    ):
        display_board(board)
        print(f"Player {player} wins!")
        break

else:
    display_board(board)
    print("It's a draw!")
