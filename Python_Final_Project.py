import random

# Tic Tac Toe

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if all(cell == "X" for cell in row) or all(cell == "O" for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == "X" for row in range(3)) or all(board[row][col] == "O" for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == "X" for i in range(3)) or all(board[i][2 - i] == "O" for i in range(3)):
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1

        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            elif all(cell != " " for row in board for cell in row):
                print_board(board)
                print("It's a tie!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("That cell is already taken!")

# Sudoku

def print_sudoku(sudoku):
    for row in sudoku:
        print(" ".join(map(str, row)))

def is_valid_move(sudoku, row, col, num):
    # Check row
    if num in sudoku[row]:
        return False

    # Check column
    if num in [sudoku[i][col] for i in range(9)]:
        return False

    # Check 3x3 square
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if sudoku[i][j] == num:
                return False

    return True

def solve_sudoku(sudoku):
    empty_cell = find_empty_cell(sudoku)
    if not empty_cell:
        return True

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(sudoku, row, col, num):
            sudoku[row][col] = num
            if solve_sudoku(sudoku):
                return True
            sudoku[row][col] = 0

    return False

def find_empty_cell(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i, j)
    return None

def sudoku_game():
    sudoku = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Initial Sudoku Puzzle:")
    print_sudoku(sudoku)
    print("\nSolving Sudoku...")
    if solve_sudoku(sudoku):
        print("\nSolved Sudoku:")
        print_sudoku(sudoku)
    else:
        print("No solution exists for the given Sudoku puzzle.")

# Number Guessing Game

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number {secret_number} in {attempts} attempts!")
            break

# Main Menu

def main():
    print("Welcome to the Game Suite!")
    while True:
        print("\nChoose a game:")
        print("1. Tic Tac Toe")
        print("2. Sudoku")
        print("3. Number Guessing Game")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            tic_tac_toe()
        elif choice == "2":
            sudoku_game()
        elif choice == "3":
            number_guessing_game()
        elif choice == "4":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
