def sudoku_grid_correct(sudoku: list):
    for row in range(len(sudoku)):
        if row_correct(sudoku, row) == False:
            return False
    for col in range(len(sudoku[0])):
        if column_correct(sudoku, col) == False:
            return False
    for row in range(0, len(sudoku), 3):
        for col in range(0,len(sudoku[row]), 3):
            if block_correct(sudoku, row, col) == False:
                return False
    return True


def block_correct(sudoku: list, row_no: int, column_no: int):
    check = []
    for row in range (row_no, row_no+3):
        for col in range (column_no, column_no+3):
            check.append(sudoku[row][col])
    for val in range(1, 10):
            seen_once = False
            for num in check:
                if num == val:
                    if not seen_once:
                        seen_once = True
                    else:
                        return False
    return True

def column_correct(list : list, column_num : int):
    check = []
    for row in list:
        check.append(row[column_num])

    for val in range(1, 10):
        seen_once = False
        for num in check:
            if num == val:
                if not seen_once:
                    seen_once = True
                else:
                    return False
    return True

def row_correct(sudoku : list, row_index : int):
    
    check = sudoku[row_index]
    for val in range(1, 10):
        seen_once = False
        for num in check:
            if num == val:
                if not seen_once:
                    seen_once = True
                else:
                    return False
    return True



if __name__ == "__main__":

    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
        ]

    print(sudoku_grid_correct(sudoku2))

    sudoku = [
        [ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
        [ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
        [ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
        [ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
        [ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
        [ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
        [ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
        [ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
        [ 3, 0, 1, 5, 0, 6, 4, 9, 0 ],
        ]
    print(sudoku_grid_correct(sudoku))