import random
import os
import time
from saper_data import *
import custom_std


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


def fill_grid(arr: list, size_r: int = 10, size_c: int = 10) -> list:
    for i in range(size_r):
        arr_temp = []
        for j in range(size_c):
            arr_temp.append(sym_field)
        arr.append(arr_temp)
    return arr


def fill_bombs(arr: list, size_r: int = 10, size_c: int = 10, bomb_n: int = 8) -> list:
    for i in range(size_r):
        arr_temp = []
        for j in range(size_c):
            arr_temp.append('-')
        arr.append(arr_temp)

    for i in range(bomb_n):
        row_bomb = random.randrange(0, size_r)
        col_bomb = random.randrange(0, size_c)
        arr[row_bomb][col_bomb] = sym_bomb
    return arr


def num_bombs(row_player: int, col_player: int, arr_bomb: list) -> str:
    ind_num = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if 0 <= (i + row_player) <= 18 and 0 <= (j + col_player) <= 18:
                if arr_bomb[i+row_player][j+col_player] == sym_bomb:
                    ind_num += 1
    return str(ind_num)


def in_position(menu_f: dict, arr_grid: list, arr_bomb: list) -> bool:
    print_grid(arr_grid)
    print(menu_f[0][0])

    row_player = int(input('\trow -> '))
    col_player = int(input('\tcol -> '))
    os.system('CLS')

    if arr_bomb[row_player][col_player] == sym_bomb:
        arr_grid[row_player][col_player] = sym_bomb
        print_grid(arr_grid)
        return True
    else:
        arr_grid[row_player][col_player] = num_bombs(row_player, col_player, arr_bomb)
        print_grid(arr_grid)
        return False


def mark_bomb(menu_f: dict, arr_grid: list, arr_bomb: list) -> bool:
    print_grid(arr_grid)
    print(menu_f[1][0])

    row_bomb = int(input('\trow -> '))
    col_bomb = int(input('\tcol -> '))
    arr_grid[row_bomb][col_bomb] = marker_bomb

    os.system('CLS')
    print_grid(arr_grid)

    return False


def check_in_values(arr: list, bombs_in: int, row_in: int, col_in: int) -> bool:
    if arr[1] < bombs_in < arr[2] and arr[3] < row_in < arr[4] and arr[5] < col_in < arr[6]:
        return custom_std.linear_interpolation(9 * 9, 24 * 30, row_in * col_in, 10, 668, bombs_in)

    print('one of data is out of range for:'
          '\n\t BOMBS -> {}\n\t HEIGHT -> {}\n\t WIDTH -> {}'.format(bombs_in, row_in, col_in))
    return False

def start_game() -> tuple:
    logic = False

    print('\tSTART')
    print(name_bomb)
    ind = custom_std.menu_function(menu_parameter, 'parameter')

    while not logic:
        if ind == 3:
            print('\t', name_bomb, end=' ')
            bombs_num = int(input(str(menu_parameter[ind][1]) + ' - ' + str(menu_parameter[ind][2]) + ' -> '))
            print('\t', row, end=' ')
            size_row = int(input(str(menu_parameter[ind][3]) + ' - ' + str(menu_parameter[ind][4]) + ' -> '))
            print('\t', col, end=' ')
            size_col = int(input(str(menu_parameter[ind][5]) + ' - ' + str(menu_parameter[ind][6]) + ' -> '))

            logic = check_in_values(menu_parameter[ind], bombs_num, size_row, size_col)
            time.sleep(2)
            os.system('CLS')
            # linear_interpolation(x1, x2, x, y1, y2, y) for check quantity of bombs due to custom grid
        else:
            bombs_num = menu_parameter[ind][1]
            size_row = menu_parameter[ind][2]
            size_col = menu_parameter[ind][3]
            logic = True

    print(bombs_num, size_row, size_col)
    arr_grid = []
    arr_bomb = []

    arr_grid = fill_grid(arr_grid, size_row, size_col)
    arr_bomb = fill_bombs(arr_bomb, size_row, size_col, bombs_num)
    print_grid(arr_grid)
    print_grid(arr_bomb)
    print()

    return arr_grid, arr_bomb
