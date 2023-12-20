import random

sudoku = [
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


def isDuplicateInRow(row, number):
    return number in row

def isDuplicateInColumn(col, number):
    for row in sudoku:
        if row[col] == number:
            return True
    return False

def isDuplicateInBox(row, col, number):
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if sudoku[i][j] == number:
                return True
    return False

def isValidPlacement(row, column, number):
    return not isDuplicateInRow(sudoku[row], number) and not isDuplicateInColumn(column, number) and not isDuplicateInBox(row, column, number)

def findEmptyCell():
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                return row, col
    return None

def solveSudoku():
    cell = findEmptyCell()

    if cell is None:
        return True

    row, col = cell

    for number in random.sample(range(1, 10), 9):
        if isValidPlacement(row, col, number):
            sudoku[row][col] = number

            if solveSudoku():
                return True

            sudoku[row][col] = 0

    return False

def sudokuGenerator():
    solveSudoku()



sudokuGenerator()

def createEmptyCells(totalEmptyCells,difficulty):
    emptyCells = []
    for i in range(0,9):
        if difficulty == "Schwer":
            emptyCells.append(random.randint(2,8))
        else:
            emptyCells.append(random.randint(2,5))
    while sum(emptyCells) != totalEmptyCells:
        if sum(emptyCells) > totalEmptyCells:
            max_number = emptyCells.index(max(emptyCells))
            emptyCells[max_number] -= 1
        else:
            if sum(emptyCells) < totalEmptyCells:
                min_number = emptyCells.index(min(emptyCells))
                emptyCells[min_number] += 1
    return emptyCells




def emtpyCells(difiilcuty):
    if difiilcuty == "Leicht":
        totalEmptyCells = 44
    elif difiilcuty == "Mittel":
        totalEmptyCells = 50
    else:
        totalEmptyCells = 52
    return createEmptyCells(totalEmptyCells,difiilcuty)


def zerosInSudoku(difficulty="Leicht"):

    emtpyCellsCount = emtpyCells(difficulty)

    for i in range(0,9):
        emptyCells = random.sample([0,1,2,3,4,5,6,7,8], emtpyCellsCount[i])
        for k in range(0,len(emptyCells) - 1):
            sudoku[i][emptyCells[k]] = 0
    return sudoku



