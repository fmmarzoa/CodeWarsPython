def get_generation(cells, generations):
    next_gen = list(map(list, cells))
    while generations:
        prev_gen = list(map(list, next_gen))
        print(str(generations) + ". " + str(prev_gen))
        for row in range(0, len(prev_gen)):
            row_width = len(prev_gen[row])
            for col in range(0, row_width):
                nbh_top = row - 1 if row != 0 else 0
                nbh_left = col - 1 if col != 0 else 0
                nbh_bottom = row + 1 if row != len(prev_gen) - 1 else len(prev_gen) - 1
                nbh_right = col + 1 if col != row_width - 1 else row_width - 1
                alive_neighbors = -1 if prev_gen[row][col] else 0
                for nbh_row in range(nbh_top, nbh_bottom + 1):
                    for nbh_col in range(nbh_left, nbh_right + 1):
                        if prev_gen[nbh_row][nbh_col]:
                            alive_neighbors += 1
                if prev_gen[row][col] == 0:
                    next_gen[row][col] = 1 if (alive_neighbors == 3) else 0
                else:
                    next_gen[row][col] = 1 if (4 > alive_neighbors > 1) else 0
        generations -= 1
    print(str(generations) + ". " + str(next_gen))
    return next_gen
