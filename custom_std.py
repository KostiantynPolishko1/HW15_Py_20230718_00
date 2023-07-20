import os


def menu_function(menu_f: dict) -> int:
    ind = 0
    while True:
        for i in range(len(menu_f)):
            if i == ind:
                print('-> ', menu_f[i][0])
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
            ind = 1
        elif ind > 1:
            ind = 0
