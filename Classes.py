import time

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image
from numba import jit


@jit(cache=True, nopython=True, fastmath=True)
def move_straight(pos, increment, b1, b2, b3, color, boundary_LT, white_positions, black_positions, enemy_king):
    arr = []
    if color == 'white':
        # go direction
        nn = 0
        available = True
        while available:
            # check if not already upper border
            bb = boundary_LT[(pos + nn * increment)]
            if not (bb == b1 or bb == b2 or bb == b3):
                nn = nn + 1
                # check if no own figure is in the way
                if white_positions[pos + nn * increment] == 0:
                    if black_positions[pos + nn * increment] == 0:
                        arr.append(pos + nn * increment)
                    elif black_positions[pos + nn * increment] != enemy_king:
                        arr.append(pos + nn * increment)
                        available = False
                    else:
                        available = False
                else:
                    available = False
            else:
                available = False
        return arr

    elif color == 'black':
        # go direction
        nn = 0
        available = True
        while available:
            # check if not already upper border
            bb = boundary_LT[(pos + nn * increment)]
            if not (bb == b1 or bb == b2 or bb == b3):
                nn = nn + 1
                # check if no own figure is in the way
                if black_positions[pos + nn * increment] == 0:
                    if white_positions[pos + nn * increment] == 0:
                        arr.append(pos + nn * increment)
                    elif white_positions[pos + nn * increment] != enemy_king:
                        arr.append(pos + nn * increment)
                        available = False
                    else:
                        available = False
                else:
                    available = False
            else:
                available = False
        return arr


@jit(cache=True, nopython=True, fastmath=True)
def move_diagonal(pos, increment, b1, b2, b3, b4, b5, color, boundary_LT, white_positions, black_positions, enemy_king):
    arr = []
    if color == 'white':
        # go direction
        nn = 0
        available = True
        while available:
            # check if not already upper border
            bb = boundary_LT[pos + nn * increment]
            if not (bb == b1 or bb == b2 or bb == b3 or bb == b4 or bb == b5):
                nn = nn + 1
                # check if no own figure is in the way
                if white_positions[pos + nn * increment] == 0:
                    if black_positions[pos + nn * increment] == 0:
                        arr.append(pos + nn * increment)
                    elif black_positions[pos + nn * increment] != enemy_king:
                        arr.append(pos + nn * increment)
                        available = False
                    else:
                        available = False
                else:
                    available = False
            else:
                available = False
        return arr

    elif color == 'black':
        # go direction
        nn = 0
        available = True
        while available:
            # check if not already upper border
            bb = boundary_LT[(pos + nn * increment)]
            if not (bb == b1 or bb == b2 or bb == b3 or bb == b4 or bb == b5):
                nn = nn + 1
                # check if no own figure is in the way
                if black_positions[pos + nn * increment] == 0:
                    if white_positions[pos + nn * increment] == 0:
                        arr.append(pos + nn * increment)
                    elif white_positions[pos + nn * increment] != enemy_king:
                        arr.append(pos + nn * increment)
                        available = False
                    else:
                        available = False
                else:
                    available = False
            else:
                available = False
        return arr


@jit(cache=True, nopython=True, fastmath=True)
def move_pawn(pos, boundary, color, black_positions, white_positions, enemy_king, already_moved, index):
    arr = []
    if color == 'white':
        # normal field no boundary
        if boundary > 8:
            if black_positions[pos + 8] == 0 and white_positions[pos + 8] == 0:
                arr.append(pos + 8)
                if already_moved == False and black_positions[pos + 16] == 0:
                    arr.append(pos + 16)
            if black_positions[pos + 7] != 0 and black_positions[pos + 7] != enemy_king:
                arr.append(pos + 7)
            if black_positions[pos + 9] != 0 and black_positions[pos + 9] != enemy_king:
                arr.append(pos + 9)
        # left border
        elif boundary == 5:
            if black_positions[pos + 8] == 0 and white_positions[pos + 8] == 0:
                arr.append(pos + 8)
                if already_moved == False and black_positions[pos + 16] == 0:
                    arr.append(pos + 16)
            if black_positions[pos + 9] != 0 and black_positions[pos + 9] != enemy_king:
                arr.append(pos + 9)
        # right border
        elif boundary == 7:
            if black_positions[pos + 8] == 0 and white_positions[pos + 8] == 0:
                arr.append(pos + 8)
                if already_moved == False and black_positions[pos + 16] == 0:
                    arr.append(pos + 16)
            if black_positions[pos + 7] != 0 and black_positions[pos + 7] != enemy_king:
                arr.append(pos + 7)
    elif color == 'black':
        # normal field no boundary
        if boundary > 8:
            if white_positions[pos - 8] == 0 and black_positions[pos - 8] == 0:
                arr.append(pos - 8)
                if already_moved == False and white_positions[pos - 16] == 0:
                    arr.append(pos - 16)
            if white_positions[pos - 7] != 0 and white_positions[pos - 7] != enemy_king:
                arr.append(pos - 7)
            if white_positions[pos - 9] != 0 and white_positions[pos - 9] != enemy_king:
                arr.append(pos - 9)
        # left border
        elif boundary == 5:
            if white_positions[pos - 8] == 0 and black_positions[pos - 8] == 0:
                arr.append(pos - 8)
                if already_moved == False and white_positions[pos - 16] == 0:
                    arr.append(pos - 16)
            if white_positions[pos - 7] != 0 and white_positions[pos - 7] != enemy_king:
                arr.append(pos - 7)
        # right border
        elif boundary == 7:
            if white_positions[pos - 8] == 0 and black_positions[pos - 8] == 0:
                arr.append(pos - 8)
                if already_moved == False and white_positions[pos - 16] == 0:
                    arr.append(pos - 16)
            if white_positions[pos - 9] != 0 and white_positions[pos - 9] != enemy_king:
                arr.append(pos - 9)

    array = np.empty((len(arr), 2), dtype=np.uint8)
    array[:, 0] = index
    array[:, 1] = np.array(arr)
    return array


@jit(cache=True, nopython=True, fastmath=True)
def move_king(pos, boundary, color, boundary_LT, black_positions, white_positions, enemy_king, already_moved, index):
    arr = []
    if color == 'white':
        ek_pos = black_positions[np.where(black_positions == enemy_king)]
    else:
        ek_pos = white_positions[np.where(white_positions == enemy_king)]

    ek_boundary = boundary_LT[ek_pos[0]]

    # get enemy king influence field
    if ek_boundary > 8:
        ek = [ek_pos + 0, ek_pos + 1, ek_pos - 1, ek_pos - 7, ek_pos - 8, ek_pos - 9, ek_pos + 7, ek_pos + 8,
              ek_pos + 9]  # not allowed positions due to enemy king
    elif ek_boundary == 8:
        ek = [ek_pos + 0, ek_pos - 1, ek_pos + 1, ek_pos + 9, ek_pos + 7, ek_pos + 8]
    elif ek_boundary == 7:
        ek = [ek_pos + 0, ek_pos - 1, ek_pos - 8, ek_pos - 9, ek_pos + 7, ek_pos + 8]
    elif ek_boundary == 6:
        ek = [ek_pos + 0, ek_pos - 1, ek_pos - 8, ek_pos - 9, ek_pos + 1, ek_pos - 7]
    elif ek_boundary == 5:
        ek = [ek_pos + 0, ek_pos + 1, ek_pos - 8, ek_pos - 7, ek_pos + 8, ek_pos + 9]
    elif ek_boundary == 4:
        ek = [ek_pos + 0, ek_pos - 1, ek_pos + 8, ek_pos + 7]
    elif ek_boundary == 3:
        ek = [ek_pos + 0, ek_pos - 1, ek_pos - 8, ek_pos - 9]
    elif ek_boundary == 2:
        ek = [ek_pos + 0, ek_pos - 8, ek_pos - 7, ek_pos + 1]
    elif ek_boundary == 1:
        ek = [ek_pos + 0, ek_pos + 1, ek_pos + 8, ek_pos + 9]

    # ek = np.array(ek, dtype=np.int32)
    def ek_intersect(position, ekk):
        for pp in ekk:
            if pp == position:
                return True
        return False

    if color == 'white':
        # normal field no boundary
        if boundary > 8:
            mov = [-9, -8, -7, +1, +9, +8, +7, -1]
            for m in mov:
                if white_positions[pos + m] == 0 and not ek_intersect(pos + m, ek):
                    arr.append(pos + m)
        elif boundary == 8:
            mov = [-1, +1, +8, +7, +9]
            for m in mov:
                if white_positions[pos + m] == 0 and not ek_intersect(pos + m, ek):
                    arr.append(pos + m)
        elif boundary == 7:
            mov = [-9, -8, +8, +7, -1]
            for m in mov:
                if white_positions[pos + m] == 0 and not ek_intersect(pos + m, ek):
                    arr.append(pos + m)
        elif boundary == 6:
            mov = [-9, -8, -7, +1, -1]
            for m in mov:
                if white_positions[pos + m] == 0 and not ek_intersect(pos + m, ek):
                    arr.append(pos + m)
        elif boundary == 5:
            mov = [-8, -7, +1, +9, +8]
            for m in mov:
                if white_positions[pos + m] == 0 and not ek_intersect(pos + m, ek):
                    arr.append(pos + m)
        elif boundary == 4:
            mov = [-1, 7, 8]
            for m in mov:
                if white_positions[pos + m] == 0 and not ek_intersect(pos + m, ek):
                    arr.append(pos + m)
        elif boundary == 3:
            mov = [-1, -8, -9]
            for m in mov:
                if white_positions[pos + m] == 0 and not ek_intersect(pos + m, ek):
                    arr.append(pos + m)
        elif boundary == 2:
            mov = [-8, -7, +1]
            for m in mov:
                if white_positions[pos + m] == 0 and not ek_intersect(pos + m, ek):
                    arr.append(pos + m)
        elif boundary == 1:
            mov = [1, 8, 9]
            for m in mov:
                if white_positions[pos + m] == 0 and not ek_intersect(pos + m, ek):
                    arr.append(pos + m)

    elif color == 'black':
        # normal field no boundary
        if boundary > 8:
            mov = [-9, -8, -7, +1, +9, +8, +7, -1]
            for m in mov:
                if black_positions[pos + m] == 0 and not ek_intersect(pos + m, ek):
                    arr.append(pos + m)
        elif boundary == 8:
            mov = [-1, +1, +8, +7, +9]
            for m in mov:
                if black_positions[pos + m] == 0 and not ek_intersect(pos + m, ek):
                    arr.append(pos + m)
        elif boundary == 7:
            mov = [-9, -8, +8, +7, -1]
            for m in mov:
                if black_positions[pos + m] == 0 and not ek_intersect(pos + m, ek):
                    arr.append(pos + m)
        elif boundary == 6:
            mov = [-9, -8, -7, +1, -1]
            for m in mov:
                if black_positions[pos + m] == 0 and not ek_intersect(pos + m, ek):
                    arr.append(pos + m)
        elif boundary == 5:
            mov = [-8, -7, +1, +9, +8]
            for m in mov:
                if black_positions[pos + m] == 0 and not ek_intersect(pos + m, ek):
                    arr.append(pos + m)
        elif boundary == 4:
            mov = [-1, 7, 8]
            for m in mov:
                if black_positions[pos + m] == 0 and not ek_intersect(pos + m, ek):
                    arr.append(pos + m)
        elif boundary == 3:
            mov = [-1, -8, -9]
            for m in mov:
                if black_positions[pos + m] == 0 and not ek_intersect(pos + m, ek):
                    arr.append(pos + m)
        elif boundary == 2:
            mov = [-8, -7, +1]
            for m in mov:
                if black_positions[pos + m] == 0 and not ek_intersect(pos + m, ek):
                    arr.append(pos + m)
        elif boundary == 1:
            mov = [1, 8, 9]
            for m in mov:
                if black_positions[pos + m] == 0 and not ek_intersect(pos + m, ek):
                    arr.append(pos + m)

    array = np.empty((len(arr), 2), dtype=np.uint8)
    array[:, 0] = index
    array[:, 1] = np.array(arr)
    return array


@jit(cache=True, nopython=True, fastmath=True)
def move_knight(pos, boundary, color, black_positions, white_positions, enemy_king, already_moved, index):
    arr = []
    boundary_val = [17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    field_values = [[-15, -6, 10, 17, 15, 6, -10, -17], [-6, 10, 17, 15, 6, -10], [-15, 17, 15, 6, -10, -17],
                    [-15, -6, 10, 6, -10, -17], [-15, -6, 10, 17, 15, -17], [17, 15, 6, -10], [-15, 6, -10, -17],
                    [-15, -6, 10, -17], [-6, 10, 17, 15], [10, 17, 15, 6], [15, 6, -10, -17], [-15, -6, -10, -17],
                    [-15, -6, 10, 17], [6, 15], [-10, -17], [-6, -15], [10, 17]]

    not_allowed = False
    if color == 'white':
        # check all boundary conditions
        for ind, b_val in enumerate(boundary_val):
            if boundary == b_val:
                for val in field_values[ind]:
                    # further checks
                    if pos == 6 and (pos + val) == 16:
                        not_allowed = True
                    elif pos == 1 and (pos + val) == 7:
                        not_allowed = True
                    elif pos == 8 and (pos + val) == -7:
                        not_allowed = True
                    elif pos == 48 and (pos + val) == 65:
                        not_allowed = True
                    elif pos == 57 and (pos + val) == 47:
                        not_allowed = True
                    elif pos == 62 and (pos + val) == 56:
                        not_allowed = True
                    elif pos == 55 and (pos + val) == 70:
                        not_allowed = True
                    elif pos == 15 and (pos + val) == -2:
                        not_allowed = True
                    else:
                        not_allowed = False

                    if not not_allowed:
                        if white_positions[pos + val] == 0 and black_positions[pos + val] != enemy_king:
                            arr.append(pos + val)
                break

    elif color == 'black':
        # check all boundary conditions
        for ind, b_val in enumerate(boundary_val):
            if boundary == b_val:
                for val in field_values[ind]:
                    # further checks
                    if pos == 6 and (pos + val) == 16:
                        not_allowed = True
                    elif pos == 1 and (pos + val) == 7:
                        not_allowed = True
                    elif pos == 8 and (pos + val) == -7:
                        not_allowed = True
                    elif pos == 48 and (pos + val) == 65:
                        not_allowed = True
                    elif pos == 57 and (pos + val) == 47:
                        not_allowed = True
                    elif pos == 62 and (pos + val) == 56:
                        not_allowed = True
                    elif pos == 55 and (pos + val) == 70:
                        not_allowed = True
                    elif pos == 15 and (pos + val) == -2:
                        not_allowed = True
                    else:
                        not_allowed = False

                    if not not_allowed:
                        if black_positions[pos + val] == 0 and white_positions[pos + val] != enemy_king:
                            arr.append(pos + val)
                break

    array = np.empty((len(arr), 2), dtype=np.uint8)
    array[:, 0] = index
    array[:, 1] = np.array(arr)
    return array


class Figure:
    def __init__(self, index, color, white_positions, black_positions, position, Lookup_Tables):
        self.index = index
        self.color = color
        self.white_positions = white_positions
        self.black_positions = black_positions
        self.current_position = position
        self.Lookup_Tables = Lookup_Tables
        self.boundary_LT = self.Lookup_Tables['boundary']
        self.position_boundary_type = self.get_boundary_type(index)
        self.already_moved = False
        if color == 'white':
            self.enemy_king = 28
        else:
            self.enemy_king = 4

    def move(self, new_position):
        # update positions array
        if self.color == 'white':
            self.white_positions[self.current_position] = 0
            self.white_positions[new_position] = self.index
        else:
            self.black_positions[self.current_position] = 0
            self.black_positions[new_position] = self.index
        # update other data
        self.current_position = new_position
        self.already_moved = True

    def get_boundary_type(self, field_id):
        return self.boundary_LT[field_id]

    def go_straight_direction(self, direction):
        pos = self.current_position

        if direction == 'up':
            return move_straight(pos, -8, 8, 1, 4, self.color, self.boundary_LT, self.white_positions,
                                 self.black_positions, self.enemy_king)
        elif direction == 'down':
            return move_straight(pos, 8, 6, 2, 3, self.color, self.boundary_LT, self.white_positions,
                                 self.black_positions, self.enemy_king)
        elif direction == 'left':
            return move_straight(pos, -1, 5, 1, 2, self.color, self.boundary_LT, self.white_positions,
                                 self.black_positions, self.enemy_king)
        elif direction == 'right':
            return move_straight(pos, 1, 7, 3, 4, self.color, self.boundary_LT, self.white_positions,
                                 self.black_positions, self.enemy_king)

    def go_diagonal_direction(self, direction):
        pos = self.current_position

        if direction == 'left_up':
            return move_diagonal(pos, -9, 5, 8, 2, 1, 4, self.color, self.boundary_LT, self.white_positions,
                                 self.black_positions, self.enemy_king)
        elif direction == 'right_up':
            return move_diagonal(pos, -7, 7, 8, 3, 1, 4, self.color, self.boundary_LT, self.white_positions,
                                 self.black_positions, self.enemy_king)
        elif direction == 'left_down':
            return move_diagonal(pos, 7, 5, 6, 1, 2, 3, self.color, self.boundary_LT, self.white_positions,
                                 self.black_positions, self.enemy_king)
        elif direction == 'right_down':
            return move_diagonal(pos, 9, 7, 6, 2, 3, 4, self.color, self.boundary_LT, self.white_positions,
                                 self.black_positions, self.enemy_king)


class Pawn(Figure):
    def __init__(self, index, color, white_positions, black_positions, position, Lookup_Tables):
        super().__init__(index, color, white_positions, black_positions, position, Lookup_Tables)

    def get_possible_movement_positions(self):
        pos = self.current_position
        boundary = self.get_boundary_type(pos)
        return move_pawn(pos, boundary, self.color, self.black_positions, self.white_positions, self.enemy_king,
                         self.already_moved, self.index)

    def check_threatenings(self):
        return 1  # return index of threatened figures if there are any


class Rook(Figure):
    def __init__(self, index, color, white_positions, black_positions, position, Lookup_Tables):
        super().__init__(index, color, white_positions, black_positions, position, Lookup_Tables)

    def get_possible_movement_positions(self):
        lists = []
        lists = lists + self.go_straight_direction('up')
        lists = lists + self.go_straight_direction('down')
        lists = lists + self.go_straight_direction('left')
        lists = lists + self.go_straight_direction('right')

        array = np.empty((len(lists), 2), dtype=np.uint8)
        array[:, 0] = self.index
        array[:, 1] = np.array(lists)
        return array  # return all possible movement positions

    def check_threatenings(self):
        return 1  # return index of threatened figures if there are any


class Bishop(Figure):
    def __init__(self, index, color, white_positions, black_positions, position, Lookup_Tables):
        super().__init__(index, color, white_positions, black_positions, position, Lookup_Tables)

    def get_possible_movement_positions(self):
        lists = []
        lists = lists + self.go_diagonal_direction('left_up')
        lists = lists + self.go_diagonal_direction('left_down')
        lists = lists + self.go_diagonal_direction('right_up')
        lists = lists + self.go_diagonal_direction('right_down')

        array = np.empty((len(lists), 2), dtype=np.uint8)
        array[:, 0] = self.index
        array[:, 1] = np.array(lists)
        return array  # return all possible movement positions

    def check_threatenings(self):
        return 1  # return index of threatened figures if there are any


class Knight(Figure):
    def __init__(self, index, color, white_positions, black_positions, position, Lookup_Tables):
        super().__init__(index, color, white_positions, black_positions, position, Lookup_Tables)

    def get_possible_movement_positions(self):
        pos = self.current_position
        boundary = self.get_boundary_type(pos)
        return move_knight(pos, boundary, self.color, self.black_positions, self.white_positions, self.enemy_king,
                           self.already_moved, self.index)

    def check_threatenings(self):
        return 1  # return index of threatened figures if there are any


class Queen(Figure):
    def __init__(self, index, color, white_positions, black_positions, position, Lookup_Tables):
        super().__init__(index, color, white_positions, black_positions, position, Lookup_Tables)

    def get_possible_movement_positions(self):
        lists = []
        lists = lists + self.go_straight_direction('up')
        lists = lists + self.go_straight_direction('down')
        lists = lists + self.go_straight_direction('left')
        lists = lists + self.go_straight_direction('right')

        lists = lists + self.go_diagonal_direction('left_up')
        lists = lists + self.go_diagonal_direction('left_down')
        lists = lists + self.go_diagonal_direction('right_up')
        lists = lists + self.go_diagonal_direction('right_down')

        array = np.empty((len(lists), 2), dtype=np.uint8)
        array[:, 0] = self.index
        array[:, 1] = np.array(lists)
        return array  # return all possible movement positions

    def check_threatenings(self):
        return 1  # return index of threatened figures if there are any


class King(Figure):
    def __init__(self, index, color, white_positions, black_positions, position, Lookup_Tables):
        super().__init__(index, color, white_positions, black_positions, position, Lookup_Tables)

    def get_possible_movement_positions(self):
        pos = self.current_position
        boundary = self.get_boundary_type(pos)
        return move_king(pos, boundary, self.color, self.boundary_LT, self.black_positions, self.white_positions,
                         self.enemy_king, self.already_moved, self.index)

    def check_threatenings(self):
        return 1  # return index of threatened figures if there are any


class Chessboard:

    def __init__(self):
        self.icon_dict = {}
        self.white_positions = np.squeeze(np.zeros((64, 1), dtype=np.uint8))
        self.black_positions = np.squeeze(np.zeros((64, 1), dtype=np.uint8))
        self.white_figures = {}
        self.black_figures = {}

    def initialize_standard_board(self, Lookup_Tables):
        self.white_positions[0:16] = np.array(range(16)) + 1
        self.black_positions[48:64] = np.array(range(16)) + 17
        # set white figures
        # Pawns
        for i in range(8):  # create white pawns
            self.white_figures[i + 9] = Pawn(i + 9, 'white', self.white_positions, self.black_positions, i + 8,
                                             Lookup_Tables)
        # Rooks
        self.white_figures[1] = Rook(1, 'white', self.white_positions, self.black_positions, 0, Lookup_Tables)
        self.white_figures[8] = Rook(8, 'white', self.white_positions, self.black_positions, 7, Lookup_Tables)
        # Knights
        self.white_figures[2] = Knight(2, 'white', self.white_positions, self.black_positions, 1, Lookup_Tables)
        self.white_figures[7] = Knight(7, 'white', self.white_positions, self.black_positions, 6, Lookup_Tables)
        # Bishops
        self.white_figures[3] = Bishop(3, 'white', self.white_positions, self.black_positions, 2, Lookup_Tables)
        self.white_figures[6] = Bishop(6, 'white', self.white_positions, self.black_positions, 5, Lookup_Tables)
        # King and Queen
        self.white_figures[4] = King(4, 'white', self.white_positions, self.black_positions, 3, Lookup_Tables)
        self.white_figures[5] = Queen(5, 'white', self.white_positions, self.black_positions, 4, Lookup_Tables)
        # set black figures
        # Pawns
        for i in range(8):  # create black pawns
            self.black_figures[i + 17] = Pawn(i + 17, 'black', self.white_positions, self.black_positions, i + 48,
                                              Lookup_Tables)
        # Rooks
        self.black_figures[25] = Rook(25, 'black', self.white_positions, self.black_positions, 56, Lookup_Tables)
        self.black_figures[32] = Rook(32, 'black', self.white_positions, self.black_positions, 63, Lookup_Tables)
        # Knights
        self.black_figures[26] = Knight(26, 'black', self.white_positions, self.black_positions, 57, Lookup_Tables)
        self.black_figures[31] = Knight(31, 'black', self.white_positions, self.black_positions, 62, Lookup_Tables)
        # Bishops
        self.black_figures[27] = Bishop(27, 'black', self.white_positions, self.black_positions, 58, Lookup_Tables)
        self.black_figures[30] = Bishop(30, 'black', self.white_positions, self.black_positions, 61, Lookup_Tables)
        # King and Queen
        self.black_figures[28] = King(28, 'black', self.white_positions, self.black_positions, 59, Lookup_Tables)
        self.black_figures[29] = Queen(29, 'black', self.white_positions, self.black_positions, 60, Lookup_Tables)

    def visualize_board(self):
        # convert chessboard indizes to pixel offsets for figure plotting on the board
        # 760 px = Board width
        # 48 px is offset, 95 px difference
        position_conversion_x = (np.array(range(64), dtype=np.uint32) % 8) * 95 + 48
        position_conversion_y = (7 - (np.floor(np.array(range(64)) / 8)).astype(int)) * 95 + 48

        # load icons if not already done
        if not bool(self.icon_dict):
            self.icon_dict['board_img'] = image.imread("visualization\\Chessboard.png")
            self.icon_dict['w_pawn_img'] = image.imread("visualization\\W_Pawn.png")
            self.icon_dict['w_knight_img'] = image.imread("visualization\\W_Knight.png")
            self.icon_dict['w_rook_img'] = image.imread("visualization\\W_Rook.png")
            self.icon_dict['w_bishop_img'] = image.imread("visualization\\W_Bishop.png")
            self.icon_dict['w_queen_img'] = image.imread("visualization\\W_Queen.png")
            self.icon_dict['w_king_img'] = image.imread("visualization\\W_King.png")
            self.icon_dict['b_pawn_img'] = image.imread("visualization\\B_Pawn.png")
            self.icon_dict['b_knight_img'] = image.imread("visualization\\B_Knight.png")
            self.icon_dict['b_rook_img'] = image.imread("visualization\\B_Rook.png")
            self.icon_dict['b_bishop_img'] = image.imread("visualization\\B_Bishop.png")
            self.icon_dict['b_queen_img'] = image.imread("visualization\\B_Queen.png")
            self.icon_dict['b_king_img'] = image.imread("visualization\\B_King.png")

        fig = plt.figure(dpi=72, figsize=(10, 10))
        ax = fig.add_subplot(111)
        ax.patch.set_alpha(0)
        ax.set_xlim((0, 4))
        ax.set_ylim((0, 4))
        fig.figimage(self.icon_dict['board_img'], 60, 60, origin="upper")

        for key in self.white_figures.keys():
            # get figure image keys
            figure = self.white_figures[key]
            if figure.__class__.__name__ == 'Pawn':
                fig_key = 'w_pawn_img'
            elif figure.__class__.__name__ == 'Rook':
                fig_key = 'w_rook_img'
            elif figure.__class__.__name__ == 'Knight':
                fig_key = 'w_knight_img'
            elif figure.__class__.__name__ == 'Bishop':
                fig_key = 'w_bishop_img'
            elif figure.__class__.__name__ == 'King':
                fig_key = 'w_king_img'
            elif figure.__class__.__name__ == 'Queen':
                fig_key = 'w_queen_img'
            # plot figure
            img = self.icon_dict[fig_key]
            x_pos = position_conversion_x[figure.current_position]
            y_pos = position_conversion_y[figure.current_position]
            isize = img.shape[1], img.shape[0]
            fig.figimage(img, 60 - (isize[0] / 2) + x_pos, 60 - (isize[1] / 2) + y_pos, origin="upper")

        for key in self.black_figures.keys():
            # get figure image keys
            figure = self.black_figures[key]
            if figure.__class__.__name__ == 'Pawn':
                fig_key = 'b_pawn_img'
            elif figure.__class__.__name__ == 'Rook':
                fig_key = 'b_rook_img'
            elif figure.__class__.__name__ == 'Knight':
                fig_key = 'b_knight_img'
            elif figure.__class__.__name__ == 'Bishop':
                fig_key = 'b_bishop_img'
            elif figure.__class__.__name__ == 'King':
                fig_key = 'b_king_img'
            elif figure.__class__.__name__ == 'Queen':
                fig_key = 'b_queen_img'
            img = self.icon_dict[fig_key]
            x_pos = position_conversion_x[figure.current_position]
            y_pos = position_conversion_y[figure.current_position]
            isize = img.shape[1], img.shape[0]
            fig.figimage(img, 60 - (isize[0] / 2) + x_pos, 60 - (isize[1] / 2) + y_pos, origin="upper")
        plt.show()

    def make_random_moves(self, number, plot=True, plot_all=False):
        for m in range(number):
            # move white
            fig = self.white_figures[np.random.randint(1, 17)]
            pos = fig.get_possible_movement_positions()
            if not isinstance(pos, int):  # only temorary check if all implemented this will no longer be needed
                if len(pos > 0):
                    pos = pos[np.random.randint(0, int(pos.size / 2)), :]
                    self.white_figures[pos[0]].move(pos[1])
                    if plot_all:
                        self.visualize_board()
            # move black
            fig = self.black_figures[np.random.randint(17, 33)]
            pos = fig.get_possible_movement_positions()
            if not isinstance(pos, int):  # only temorary check if all implemented this will no longer be needed
                if len(pos > 0):
                    pos = pos[np.random.randint(0, int(pos.size / 2)), :]
                    self.black_figures[pos[0]].move(pos[1])
                    if plot_all:
                        self.visualize_board()
        if plot:
            self.visualize_board()

    def get_all_possible_moves(self, color):
        all_moves = []
        if color == 'white':
            for key in self.white_figures.keys():
                all_moves.append(self.white_figures[key].get_possible_movement_positions())
        else:
            for key in self.black_figures.keys():
                all_moves.append(self.black_figures[key].get_possible_movement_positions())
        return all_moves
