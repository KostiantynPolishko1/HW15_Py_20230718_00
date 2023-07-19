def num_bombs(row: int, col: int, arr_bomb: list, sym_bomb: str) -> str:
    ind_num = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if 0 <= (i + row) <= 18 and 0 <= (j + col) <= 18:
                if arr_bomb[i+row][j+col] == sym_bomb:
                    ind_num += 1
    return str(ind_num)
