import saper
import custom_std

# Task1 GAME SUPER

if __name__ == '__main__':
    num_bomb, num_marker, size_grid = 8, 8, 10
    sym_bomb, marker_bomb, sym_field = 'X', 'B', '*'
    menu_f = {0: ['open CELL', False, saper.in_position],
              1: ['mark BOMB', True, saper.mark_bomb]}

    arr_grid, arr_bomb = saper.start_game(num_bomb, size_grid)

    while True:
        if menu_f[custom_std.menu_function(menu_f)][2](menu_f, arr_grid, arr_bomb, sym_bomb, marker_bomb):
            print('GAME OVER')
            break
else:
    print('ERROR')
