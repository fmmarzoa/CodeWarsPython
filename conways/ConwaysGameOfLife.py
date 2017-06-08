import numpy as np


def get_neighbourhood(arr, row, col):
    """Returns the complete neighbour for the cell 
       at row, col in the array arr"""
    top = row - 1 if row > 0 else 0
    bottom = row + 1 if row < arr.shape[0] - 1 else arr.shape[0]
    left = col - 1 if col > 0 else 0
    right = col + 1 if col < arr.shape[1] - 1 else arr.shape[1]
    return arr[top:bottom+1, left:right+1]


def crop_array(arr):
    """Removes columns and rows with only zeroes 
       on outside margins"""
    while arr.size and np.count_nonzero(arr[0]) == 0:
        # Remove rows from top to bottom until we find a non-zero one
        arr = arr[1:]
    while arr.size and np.count_nonzero(arr[-1]) == 0:
        # Remove rows from bottom to top until we find a non-zero one
        arr = arr[:-1]
    while arr.size and np.count_nonzero(arr[0:, 0]) == 0:
        # Remove rows from left to right until we find a non-zero one
        arr = arr[0:, 1:]
    while arr.size and np.count_nonzero(arr[0:, -1]) == 0:
        # Remove rows from right to left until we find a non-zero one
        arr = arr[0:, :-1]
    return arr


def get_generation(cells, generations):
    print ("gens:" + str(generations) + "\ncells: " + str(cells))
    current_gen = np.array(cells)
    # Create a new zero-filled matrix two rows and columns wider
    next_gen = np.zeros((current_gen.shape[0] + 2, current_gen.shape[1] + 2), dtype=np.int)
    # Insert the current generation matrix in the middle of the next generation one
    next_gen[1:current_gen.shape[0] + 1, 1:current_gen.shape[1] + 1] = current_gen
    while generations:
        current_gen = np.array(next_gen)
        for row in range(0, current_gen.shape[0]):
            for col in range(0, current_gen.shape[1]):
                neighbourhood = get_neighbourhood(current_gen, row, col)
                alive_neighbours = np.count_nonzero(neighbourhood)
                if current_gen[row, col]:
                    # Cell is alive
                    # Remove the cell we are checking itself from the alive_neighbours count
                    alive_neighbours -= 1
                    if alive_neighbours > 3 or alive_neighbours < 2:
                        # Kill the cell if there are more than 3 or less than 2 neighbours alive
                        next_gen[row, col] = 0
                else:
                    # Cell is dead
                    if alive_neighbours == 3:
                        # Revive cell if there are exactly three neighbours alive
                        next_gen[row, col] = 1
        generations -= 1
    return crop_array(next_gen).tolist()
