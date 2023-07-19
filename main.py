import os
import saper

# Task1 GAME SAPER

if __name__ == '__main__':
    num_bomb, num_marker, size_grid = 8, 8, 10
    sym_bomb, marker_bomb = 'x', 'B'
    arr_grid, arr_bomb = saper.start_game(num_bomb, size_grid)

    while True:
        saper.print_grid(arr_grid)
        if saper.mark_bomb(arr_grid, marker_bomb):
            os.system('CLS')
            continue

        saper.print_grid(arr_grid)
        logic = saper.in_position(arr_grid, arr_bomb, sym_bomb)
        os.system('CLS')
        if logic:
            saper.print_grid(arr_grid)
            print('GAME OVER')
            break
else:
    print('ERROR')