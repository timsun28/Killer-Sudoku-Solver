def transform_json_to_correct(json):
    # Json doesn't allow tuples to be stored. This function transforms the lists in 'boxes' to tuples.
    for cage in json:
        cage['boxes'] = [tuple(box) for box in cage['boxes']]
    return json


def check_input(cages):
    # Check if there are no double coordinates by creating a list with all the coordinates and transforming it to a set.
    cages_cells = [item for cage in cages for item in cage['boxes']]
    if len(cages_cells) != len(set(cages_cells)):
        print('There are double coordinates in your json. Fix this before continuing')

    # Adds all the totalSum values to an empty grid to easily display them
    grid = [[0 for i in range(0, 9)] for i in range(0, 9)]
    for cage in cages:
        for box_y, box_x in cage['boxes']:
            grid[box_y][box_x] = cage['totalSum']
    print_board(grid, zfill=2)


def print_board(grid, zfill=1):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(str(grid[i][j]).zfill(zfill))
            else:
                print(str(grid[i][j]).zfill(zfill) + " ", end="")
