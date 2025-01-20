"""
    This module contains all the functions used in the tic_tac_toe.py file.
"""

import os


def option_validator():
    """
        Validates player input. Refuses anything not in the list of options
        and returns the selected option, a single char.
    """

    options = ['1', '2', '3', 'q']
    selected = ' '
    while selected not in options:
        selected = input("'1', '2', '3', or 'q' to quit: ")

    return selected


def grid_update(grid, row, col, char):
    """
        This function updates the grid with the given positions. It returns
        the updated grid.
    """

    if grid[row][col] == ' ':
        grid[row][col] = char

    return grid


def check_empty(grid, row, col):
    """
        This function checks if the chosen position is empty. It returns True
        if empty, False if not empty.
    """

    if grid[row][col] == ' ':
        return True
    else:
        return False


def check_gameover(grid, char):
    """
        This function checks all the conditions for a gameover. It returns
        True if any of the possible states are met.
    """

    # checking the rows
    for row in grid:
        if row.count(char) == 3:
            return True

    # we can do the same if the grid is transposed
    transposed = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(grid)):
        for j in range(len(grid)):
            transposed[i][j] = grid[j][i]
    for row in transposed:
        if row.count(char) == 3:
            return True

    # now the diagonals
    d1 = []
    for i in range(len(grid)):
        d1.append(grid[i][i])
    if d1.count(char) == 3:
        return True

    # the anti-diagonal
    d2 = []
    for i in range(len(grid)):
        for j in reversed(range(len(grid))):
            if i + j == len(grid) - 1:
                d2.append(grid[i][j])
    if d2.count(char) == 3:
        return True


def display(grid_map):
    """ This function tries to show the game grid in a larger grid. It
    receives the grid_map from the function grid_mapping() and organizes
    the elements, printing line by line.
    """

    # clean up the display first:
    os.system('cls' if os.name == 'nt' else 'clear')

    # it took me hours to come up with this abomination
    for i in range(0, 6, 1):
        print(f"{grid_map[i]} | {grid_map[i + 6]} | {grid_map[i + 12]}")
        if i == 5:
            print(24 * '-')
    for i in range(18, 24, 1):
        print(f"{grid_map[i]} | {grid_map[i + 6]} | {grid_map[i + 12]}")
        if i == 23:
            print(24 * '-')
    for i in range(36, 42, 1):
        print(f"{grid_map[i]} | {grid_map[i + 6]} | {grid_map[i + 12]}")


def grid_mapping(grid):
    """ This function maps the game grid to the larger ascii
        characters bellow. It returns a simple list.
    """

    # I want the game to look bigger in the terminal
    x_cell = [
        "#    #",
        " #  # ",
        "  ##  ",
        "  ##  ",
        " #  # ",
        "#    #"
        ]

    o_cell = [
        " #### ",
        "#    #",
        "#    #",
        "#    #",
        "#    #",
        " #### "
        ]

    empty_cell = [
        "      ",
        "      ",
        "      ",
        "      ",
        "      ",
        "      ",
        ]

    # this matrix will be filled with the characters above
    matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        ]

    # mapping the matrix to the grid
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 'x':
                matrix[i][j] = x_cell
            elif grid[i][j] == 'o':
                matrix[i][j] = o_cell
            else:
                matrix[i][j] = empty_cell

    # unpacks the matrix into a simple list
    grid_map = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            for k in range(6):
                grid_map.append(matrix[i][j][k])

    return grid_map


def show_empty_grid():
    """
        In case the player starts first, this shows an empty grid.
    """

    os.system('cls' if os.name == 'nt' else 'clear')
    bar = 24 * '-'
    for i in range(20):
        if i == 6 or i == 13:
            print(bar)
        else:
            print('       |        |       ')
