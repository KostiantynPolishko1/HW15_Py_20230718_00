import random
import saper_fun

def print_grid(arr: list) ->None:
    for i in range(len(arr)):
        print(i, end=' | ')
        for j in range(len(arr)):
            print(arr[i][j], end=' | ')
        print()

    print('  | ', end='')
    for i in range(len(arr)):
        print(i, end=' | ')
    print('\n')

def fill_grid(arr: list, size: int = 10) ->list:
    for i in range(size):
        arr_temp = []
        for j in range(size):
            arr_temp.append('*')
        arr.append(arr_temp)
    return arr

def fill_bombs(arr: list, size: int = 10, num: int = 8) ->list:
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

def in_position(arr_grid: list, arr_bomb: list, sym_bomb: str) ->bool:
    print('enter position')
    row = int(input('\trow -> '))
    col = int(input('\tcol -> '))

    if arr_bomb[row][col] == 'x':
        arr_grid[row][col] = 'x'
        return True
    else:
        arr_grid[row][col] = saper_fun.num_bombs(row, col, arr_bomb, sym_bomb)
        return False

def start_game(n_bombs: int, size: int) ->tuple:
    print('GAME SAPER\n\tSTART')
    arr_grid = []
    arr_bomb = []

    arr_grid = fill_grid(arr_grid, size)
    arr_bomb = fill_bombs(arr_bomb, size, n_bombs)
    print_grid(arr_bomb)
    print()

    return arr_grid, arr_bomb
