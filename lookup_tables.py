import numpy as np


def get_boundary_LT():
    boundarys = np.squeeze(np.ones((64, 1), dtype=np.uint8)) * 17
    boundarys[np.array([0, 7, 56, 63])] = np.array([1, 4, 2, 3])  # outer corner
    boundarys[np.array([9, 14, 49, 54])] = np.array([9, 12, 10, 11])  # inner corner
    boundarys[np.array([8, 16, 24, 32, 40, 48])] = 5  # left outer
    boundarys[np.array([57, 58, 59, 60, 61, 62])] = 6  # down outer
    boundarys[np.array([15, 23, 31, 39, 47, 55])] = 7  # right outer
    boundarys[np.array([1, 2, 3, 4, 5, 6])] = 8  # up outer
    boundarys[np.array([17, 25, 33, 41])] = 13  # left inner
    boundarys[np.array([50, 51, 52, 53])] = 14  # down inner
    boundarys[np.array([22, 30, 38, 46])] = 15  # right inner
    boundarys[np.array([10, 11, 12, 13])] = 16  # up inner
    return boundarys


def get_pawn_movement_LT():
    # pawn movement
    # choose how much movements in the actual position are possible and which lookup table should therefore be used
    pawn_movement_selection_table = np.squeeze(np.ones((64, 1), dtype=np.uint8)) * 3
    pawn_movement_selection_table[
        np.array([8, 16, 24, 32, 40, 48, 15, 23, 31, 39, 47, 55])] = 2  # left and right border
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
    return (pawn_movement_selection_table, black_pawn_movement_dict)


def get_movement_LT_dict():
    LT_dict = {'pawns': get_pawn_movement_LT()}
    LT_dict['boundary'] = get_boundary_LT()
    return LT_dict
