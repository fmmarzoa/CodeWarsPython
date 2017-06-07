import numpy as np

def crop_array(arr):
    # TODO remove columns and rows with only zeroes on outside margins

def get_generation(cells, generations):
    current_gen = np.array(cells)
    next_gen = np.zeros((current_gen.shape[0] + 2, current_gen.shape[1] + 2), dtype=np.int)
    next_gen[1:current_gen.shape[1] + 1, 1:current_gen.shape[1] + 1] = current_gen
    return cells
