import saper
import custom_std

# Task1 GAME SUPER

if __name__ == '__main__':
    arr_grid, arr_bomb = saper.start_game()

    menu_open_mark = {0: ['open CELL', False, saper.in_position],
                      1: ['mark BOMB', True, saper.mark_bomb]}

    while True:
        if menu_open_mark[custom_std.menu_function(menu_open_mark)][2](menu_open_mark, arr_grid, arr_bomb):
            print('GAME OVER')
            break
else:
    print('ERROR')
