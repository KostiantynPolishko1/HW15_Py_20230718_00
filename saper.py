import random

def start_game() ->None:
    print('GAME SAPER\n\tSTART')

def print_grid(arr: list) ->None:
    for i in range(len(arr)):
        print(i, end=' | ')
        for j in range(len(arr)):
            print(arr[i][j], end=' | ')
        print()

    print('  | ', end='')
    for i in range(len(arr)):
        print(i, end=' | ')

def fill_grid(arr: list, size: int = 10) ->None:
    for i in range(size):
        arr_temp = []
        for j in range(size):
            arr_temp.append('*')
        arr.append(arr_temp)


def fill_bombs(arr: list, size: int = 10, num: int = 8) ->None:
    for i in range(size):
        arr_temp = []
        for j in range(size):
            arr_temp.append('*')
        arr.append(arr_temp)

    for i in range(num):
        row = random.randrange(0, 9)
        col = random.randrange(0, 9)
        arr[row][col] = 'x'

def in_position(arr_grid, arr_bomb) ->bool:
    print('enter position')
    row = int(input('\trow -> '))
    col = int(input('\tcol -> '))

    if arr_bomb[row][col] == 'x':
        arr_grid[row][col] = 'x'
        return True
    else:
        arr_grid[row][col] = '-'
        return False


