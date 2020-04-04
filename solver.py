import sys
import json
from div_funcs import transform_json_to_correct, check_input, print_board
from solve_funcs import possible

filename = sys.argv[1]
sudoku_cages_from_json = json.load(open(filename))

transformed_sudoku_cages = transform_json_to_correct(sudoku_cages_from_json)

check_input(transformed_sudoku_cages)
input('Is the following correct? Press enter to continue...')

grid = [[0 for i in range(0, 9)] for i in range(0, 9)]

cage_index = {box: cage for cage in transformed_sudoku_cages for box in cage['boxes']}


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n, grid, cage_index):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print_board(grid)
    input('Press for enter to continue searching ...')


solve()
