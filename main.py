import os
import time
import saper

# Task1 GAME SAPER

if __name__ == '__main__':
    num_bomb = 8
    sym_bomb = 'x'
    size_grid = 10
    arr_grid, arr_bomb = saper.start_game(num_bomb, size_grid)

    while True:
        print('GAME SAPER')
        saper.print_grid(arr_grid)
        logic = saper.in_position(arr_grid, arr_bomb, sym_bomb)
        os.system('CLS')
        if logic:
            saper.print_grid(arr_grid)
            print('GAME OVER')
            break
else:
    print('ERROR')
