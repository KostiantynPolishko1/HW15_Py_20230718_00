import os
def num_bombs(row: int, col: int, arr_bomb: list, sym_bomb: str) -> str:
    ind_num = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if 0 <= (i + row) <= 18 and 0 <= (j + col) <= 18:
                if arr_bomb[i+row][j+col] == sym_bomb:
                    ind_num += 1
    return str(ind_num)

def menu_yn() -> bool:
    ind = 0
    arr_yn = [['yes', True], ['no', False]]
    while True:
        for i in range(len(arr_yn)):
            if i == ind:
                print('-> ', arr_yn[i][0])
                continue
            print('   ', arr_yn[i][0])

        print("\t\"w\" - Down, \"s\" - Up: ->", end='')
        direct = input(" ").lower()
        os.system('CLS')
        # increment & decrement
        if not direct:
            return arr_yn[ind][1]
        elif direct == 'w':
            ind += 1
        elif direct == 's':
            ind -= 1
        else:
            print("ERROR!")
            continue

        # check position
        if ind < 0:
            ind = 1
        elif ind > 1:
            ind = 0
