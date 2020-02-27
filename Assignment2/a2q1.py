def createGridFromLines(lines):
    """
    Purpose: Creates a grid (list) of integers from the file of sudoku puzzles.
    Pre-Conditions:
    :param lines: Each line of the grid
    Post-Conditions: none
    :return: a grid (list) of integers from sudoku puzzle file
    """
    grid = []
    for l in lines:
        l = [int(x) for x in l.split()]
        grid.append(l)
    return grid

def verify_rows(grid):
    """
    Purpose: verifies that each row is composed of non-repeating integers no bigger than 9 and no less than 1.
    Pre-Conditions:
    :param grid: Full list of the integers
    Post-Conditions: none
    :return: False if it doesnt follow conditions listed in the purpose.
    """
    verified = True
    for row in range(9):
        values = set()
        for col in range(9):
            v = grid[row][col]
            if v < 1 or v > 9 or v in values:
                print('No')
                verified = False
                break
            values.add(v)
    return verified

def verify_cols(grid):
    """
    Purpose: verifies that each column is composed of non-repeating integers no bigger than 9 and no less than 1.
    Pre-Conditions:
    :param grid: Full list of the integers
    Post-Conditions: none
    :return: False if it doesnt follow conditions listed in the purpose.
    """
    verified = True
    for col in range(9):
        values = set()
        for row in range(9):
            v = grid[row][col]
            if v < 1 or v > 9 or v in values:
                print('No')
                verified = False
                break

            values.add(v)

    return verified




def check_sudoku(file_name):
    '''
    Purpose: Checks if input file is valid and creates a grid that it verifies.
    Pre-conditions:
    :param file_name: a user input file
    Post-conditions: none
    :return: True if follows conditions of row and column functions.
    '''
    try:
        lines = open(file_name).readlines()
        grid = createGridFromLines(lines)

        if not verify_rows(grid):
            return
        if not verify_cols(grid):
            return
        print('Yes')

    except IOError:
        print('Could not open the file')


file_name = input('Enter file name: ')
check_sudoku(file_name)
