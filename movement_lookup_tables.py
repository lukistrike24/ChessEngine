import numpy as np


def get_pawn_movement_LT():
    # pawn movement
    # choose how much movements in the actual position are possible and which lookup table should therefore be used
    pawn_movement_selection_table = np.squeeze(np.ones((64, 1), dtype=np.uint8)) * 3
    pawn_movement_selection_table[
        np.array([8, 16, 24, 32, 40, 48, 15, 23, 31, 39, 47, 55])] = 2  # left and right border
    # aa = pawn_movement_selection_table.reshape(8, 8)
    black_pawn_movement_dict = {}
    white_pawn_movement_dict = {}
    arr = np.tile(np.array(range(64), dtype=np.uint8), (2, 1)).T
    arr[:, 0] = arr[:, 0] - 8
    arr[np.array([8, 16, 24, 32, 40, 48]), 1] = arr[np.array([8, 16, 24, 32, 40, 48]), 1] - 7
    arr[np.array([15, 23, 31, 39, 47, 55]), 1] = arr[np.array([15, 23, 31, 39, 47, 55]), 1] - 9
    black_pawn_movement_dict[2] = np.copy(arr)
    arr = np.tile(np.array(range(64), dtype=np.uint8), (3, 1)).T
    arr[:, 0] = arr[:, 0] - 9
    arr[:, 1] = arr[:, 1] - 8
    arr[:, 2] = arr[:, 2] - 7
    black_pawn_movement_dict[3] = np.copy(arr)
    return pawn_movement_selection_table, black_pawn_movement_dict
