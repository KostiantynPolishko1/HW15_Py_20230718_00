import saper

# Task1 GAME SAPER

if __name__ == '__main__':
    arr_grid = []
    arr_bomb = []
    saper.start_game()
    print()
    saper.fill_grid(arr_grid)
    saper.print_grid(arr_grid)

    print('\n')
    saper.fill_bombs(arr_bomb)
    saper.print_grid(arr_bomb)

    while True:
        print('\n')
        logic = saper.in_position(arr_grid, arr_bomb)
        saper.print_grid(arr_grid)
        if logic:
            break
    print('\nEND of GAME')

