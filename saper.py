import random
import os


def print_grid(arr: list) -> None:
    print('GAME SUPER')
    for i in range(len(arr)):
        print(i, end=' | ')
        for j in range(len(arr)):
            print(arr[i][j], end=' | ')
        print()

    print('  | ', end='')
    for i in range(len(arr)):
        print(i, end=' | ')
    print('\n')


def fill_grid(arr: list, size: int = 10) -> list:
    for i in range(size):
        arr_temp = []
        for j in range(size):
            arr_temp.append('*')
        arr.append(arr_temp)
    return arr


def fill_bombs(arr: list, size: int = 10, num: int = 8) -> list:
    for i in range(size):
        arr_temp = []
        for j in range(size):
            arr_temp.append('*')
        arr.append(arr_temp)

    for i in range(num):
        row = random.randrange(0, 9)
        col = random.randrange(0, 9)
        arr[row][col] = 'x'
    return arr


def num_bombs(row: int, col: int, arr_bomb: list, sym_bomb: str) -> str:
    ind_num = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if 0 <= (i + row) <= 18 and 0 <= (j + col) <= 18:
                if arr_bomb[i+row][j+col] == sym_bomb:
                    ind_num += 1
    return str(ind_num)


def in_position(menu_f: dict, arr_grid: list, arr_bomb: list, sym_bomb: str = 'X', marker_bomb: str = 'B') -> bool:
    print_grid(arr_grid)
    print(menu_f[0][0])

    row = int(input('\trow -> '))
    col = int(input('\tcol -> '))
    os.system('CLS')

    if arr_bomb[row][col] == 'x':
        arr_grid[row][col] = 'x'
        print_grid(arr_grid)
        return True
    else:
        arr_grid[row][col] = num_bombs(row, col, arr_bomb, sym_bomb)
        print_grid(arr_grid)
        return False


def mark_bomb(menu_f: dict, arr_grid: list, arr_bomb: list, sym_bomb: str = 'X', marker_bomb: str = 'B') -> bool:
    print_grid(arr_grid)
    print(menu_f[1][0])

    row = int(input('\trow -> '))
    col = int(input('\tcol -> '))
    arr_grid[row][col] = marker_bomb

    os.system('CLS')
    print_grid(arr_grid)

    return False


def start_game(n_bombs: int, size: int) -> tuple:
    print('\tSTART')
    arr_grid = []
    arr_bomb = []

    arr_grid = fill_grid(arr_grid, size)
    arr_bomb = fill_bombs(arr_bomb, size, n_bombs)
    print_grid(arr_grid)
    print_grid(arr_bomb)
    print()

    return arr_grid, arr_bomb
