import numpy as np


def get_neighbourhood(array, row, col):
    """Returns the complete neighbour for the cell 
       at row, col in the array"""
    top = row - 1 if row > 0 else 0
    bottom = row + 1 if row < array.shape[0] - 1 else array.shape[0]
    left = col - 1 if col > 0 else 0
    right = col + 1 if col < array.shape[1] - 1 else array.shape[1]
    return array[top:bottom + 1, left:right + 1]


def crop_array(array):
    """Removes columns and rows with only zeroes 
       on outside margins"""
    cropped = np.array(array)
    while cropped.size and np.count_nonzero(cropped[0]) == 0:
        # Remove rows from top to bottom until we find a non-zero one
        cropped = cropped[1:]
    while cropped.size and np.count_nonzero(cropped[-1]) == 0:
        # Remove rows from bottom to top until we find a non-zero one
        cropped = cropped[:-1]
    while cropped.size and np.count_nonzero(cropped[0:, 0]) == 0:
        # Remove rows from left to right until we find a non-zero one
        cropped = cropped[0:, 1:]
    while cropped.size and np.count_nonzero(cropped[0:, -1]) == 0:
        # Remove rows from right to left until we find a non-zero one
        cropped = cropped[0:, :-1]
    return cropped


def frame_array(array):
    framed_array = np.zeros((array.shape[0] + 2, array.shape[1] + 2), dtype=np.int)
    framed_array[1:array.shape[0] + 1, 1:array.shape[1] + 1] = array
    return framed_array


def get_generation(cells, generations):
    current_gen = np.array(cells)
    while generations:
        framed_array = frame_array(current_gen)
        next_gen = np.array(framed_array)
        for row in range(0, framed_array.shape[0]):
            for col in range(0, framed_array.shape[1]):
                neighbourhood = get_neighbourhood(framed_array, row, col)
                alive_neighbours = np.count_nonzero(neighbourhood)
                if framed_array[row, col]:
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
        current_gen = crop_array(next_gen)
        generations -= 1
    return current_gen.tolist()
