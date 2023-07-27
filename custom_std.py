import os
from saper_data import *


def menu_function(menu_f: dict, *name_dict: str) -> int:

    ind = 0
    while True:
        for i in range(len(menu_f)):
            if i == ind:
                print('-> ', menu_f[i][0], end='\t')
                if name_dict:
                    print('{} -> {} \n\t\t{}: {} x {} | {} x {}'.format(name_bomb, menu_f[ind][1], name_size, row,
                                                                        col, menu_f[ind][2],  menu_f[ind][3]))
                print()
                continue
            print('   ', menu_f[i][0])

        print("\t\"w\" - Down, \"s\" - Up: ->", end='')
        direct = input(" ").lower()
        os.system('CLS')
        # increment & decrement
        if not direct:
            return ind
        elif direct == 'w':
            ind += 1
        elif direct == 's':
            ind -= 1
        else:
            print("ERROR!")
            continue

        # check position
        if ind < 0:
            ind = len(menu_f)-1
        elif ind > len(menu_f)-1:
            ind = 0


def linear_interpolation(x1: int, x2: int, x: int, y1: int, y2: int, y: int) -> bool:
    if y > int(((y1+(x-x1))/(x2-x1))*(y2-y1)):
        print('enter bombs <= {}'.format(int(((y1+(x-x1))/(x2-x1))*(y2-y1))))
        return False
    return True
