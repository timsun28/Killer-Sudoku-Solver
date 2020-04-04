def possible(y, x, n, grid, cage_index):
    # Check for double values in row
    for i in range(0, 9):
        if grid[y][i] == n:
            return False

    # Check for double values in column
    for i in range(0, 9):
        if grid[i][x] == n:
            return False

    # Check for double values in square
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0+j] == n:
                return False

    # Check if cage rules are correct
    current_cage = cage_index[(y, x)]
    cage_values = list()

    # Adds all values to cage_values list.
    for box_y, box_x in current_cage['boxes']:
        # This if is required because at this point in the code the value is not stored in the grid yet.
        if box_y == y and box_x == x:
            cage_values.append(n)
        else:
            cage_values.append(grid[box_y][box_x])

    # Check if the current sum of all values is larger than the allowed totalSum
    current_sum = sum(cage_values)
    if current_sum > current_cage['totalSum']:
        return False

    # Check if all boxes have been valued
    all_valued = 0 not in cage_values
    if all_valued:
        # Check if the currentSum equals the totalSum
        if current_sum != current_cage['totalSum']:
            return False

        # It also checks if there are any double values in the cages (this is not allowed)
        double_values = len(cage_values) != len(set(cage_values))
        if double_values:
            return False

    return True
