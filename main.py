import os
import time
import saper

# Task1 GAME SAPER

if __name__ == '__main__':
    num_bombs = 8
    size_grid = 10
    arr_grid, arr_bomb = saper.start_game(num_bombs, size_grid)

    while True:
        saper.print_grid(arr_grid)
        logic = saper.in_position(arr_grid, arr_bomb)
        os.system('CLS')
        if logic:
            saper.print_grid(arr_grid)
            break
    print('\nEND of GAME')
else:
    print('ERROR')
