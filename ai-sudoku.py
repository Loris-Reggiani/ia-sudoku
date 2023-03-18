def solve_sudoku(puzzle):
    find = find_empty(puzzle)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(puzzle, i, (row, col)):
            puzzle[row][col] = i

            if solve_sudoku(puzzle):
                return True

            puzzle[row][col] = 0

    return False

def valid(puzzle, num, pos):
    # Check row
    for i in range(len(puzzle[0])):
        if puzzle[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(puzzle)):
        if puzzle[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if puzzle[i][j] == num and (i,j) != pos:
                return False

    return True

def print_board(puzzle):
    for i in range(len(puzzle)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(puzzle[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(puzzle[i][j])
            else:
                print(str(puzzle[i][j]) + " ", end="")

def find_empty(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                return (i, j)  # row, col

    return None

# Example puzzle
puzzle = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Example puzzle solution
solution = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

if solve_sudoku(puzzle):
    print_board(puzzle)
else:
    print("No solution exists.")