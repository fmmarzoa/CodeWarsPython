def get_generation(cells, generations):
    next_gen = list(map(list, cells))
    while generations:
        for row in range(0, len(cells)):
            row_width = len(cells[row])
            for col in range(0, row_width):
                nbh_top = row - 1 if row != 0 else 0
                nbh_left = col - 1 if col != 0 else 0
                nbh_bottom = row + 1 if row != len(cells) - 1 else len(cells) - 1
                nbh_right = col + 1 if col != row_width - 1 else row_width - 1
                alive_neighbors = -1 if cells[row][col] else 0
                for nbh_row in range(nbh_top, nbh_bottom + 1):
                    for nbh_col in range(nbh_left, nbh_right + 1):
                        if cells[nbh_row][nbh_col]:
                            alive_neighbors += 1
                next_gen[row][col] = 1 if (4 > alive_neighbors > 1) else 0
        generations -= 1
    return next_gen
