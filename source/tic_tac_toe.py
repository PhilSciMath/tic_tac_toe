"""
    I was searching for a small project to code after learning
    a bit of Python. Then I saw this idea of a tic tac toe game. I didn't see
    any example beforehand so it is going to be built from scratch.
"""


from random import choice
import time

import functions as fn

# who starts first?
player_turn = False
if input('Do you want to go first? [yes/no]: ').lower()[0] == 'y':
    player_turn = True


# definig the character the user will play
player_char = ''
chars = ['x', 'o']

while player_char not in chars:
    player_char = input("Do you choose 'x' or 'o'? ").lower()

# defining the character for the computer to play
for c in chars:
    if c != player_char:
        com_char = c

grid = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
        ]

# shows an empty grid if player starts first
if player_turn:
    fn.show_empty_grid()

# main game loop
while True:

    # alternating between player and computer
    if player_turn:

        print("Choose a row.")
        row = fn.option_validator()
        if row == 'q':
            break
        print("Choose a column.")
        col = fn.option_validator()
        if col == 'q':
            break

        row = int(row) - 1
        col = int(col) - 1

        # we don't update the grid unless the chosen position is empty
        if not fn.check_empty(grid, row, col):
            print("The position is not empty!\n")
            continue

        # updates the grid, then pass the turn to the computer
        grid = fn.grid_update(grid, row, col, player_char)
        player_turn = False

    else:
        # computer choice
        values = [0, 1, 2]
        com_choice = []

        # computer will choose positions untill it finds an empty one
        while True:
            com_choice.clear()
            for i in range(2):
                com_choice.append(choice(values))
            row = com_choice[0]
            col = com_choice[1]

            if fn.check_empty(grid, row, col):
                break

        # when the position is empty updates the grid, then it's player turn
        grid = fn.grid_update(grid, row, col, com_char)
        player_turn = True
        time.sleep(2)

    # shows the grid
    result = fn.grid_mapping(grid)
    fn.display(result)

    # gameover
    if fn.check_gameover(grid, com_char):
        print("\nYou lost!")
        break
    if fn.check_gameover(grid, player_char):
        print("\nYou won!")
        break



