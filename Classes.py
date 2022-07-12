import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image


class Figure:
    def __init__(self, index, color, white_positions, black_positions, position):
        self.index = index
        self.color = color
        self.white_positions = white_positions
        self.black_positions = black_positions
        self.current_position = position
        if color == 'white':
            self.enemy_king = 28
        else:
            self.enemy_king = 4

    def move(self, new_position):
        self.current_position = new_position


class Pawn(Figure):
    def __init__(self, index, color, white_positions, black_positions, position, movement_dict, movement_LT):
        super().__init__(index, color, white_positions, black_positions, position)
        self.movement_dict = movement_dict
        self.movement_LT = movement_LT

    def get_possible_movement_positions(self):
        if self.color == 'white':
            A = 1
        return 1  # return all possible movement positions

    def check_threatenings(self):
        return 1  # return index of threatened figures if there are any


class Rook(Figure):
    def __init__(self, index, color, white_positions, black_positions, position):
        super().__init__(index, color, white_positions, black_positions, position)

    def get_possible_movement_positions(self):
        return 1  # return all possible movement positions

    def check_threatenings(self):
        return 1  # return index of threatened figures if there are any


class Bishop(Figure):
    def __init__(self, index, color, white_positions, black_positions, position):
        super().__init__(index, color, white_positions, black_positions, position)

    def get_possible_movement_positions(self):
        return 1  # return all possible movement positions

    def check_threatenings(self):
        return 1  # return index of threatened figures if there are any


class Knight(Figure):
    def __init__(self, index, color, white_positions, black_positions, position):
        super().__init__(index, color, white_positions, black_positions, position)

    def get_possible_movement_positions(self):
        return 1  # return all possible movement positions

    def check_threatenings(self):
        return 1  # return index of threatened figures if there are any


class Queen(Figure):
    def __init__(self, index, color, white_positions, black_positions, position):
        super().__init__(index, color, white_positions, black_positions, position)

    def get_possible_movement_positions(self):
        return 1  # return all possible movement positions

    def check_threatenings(self):
        return 1  # return index of threatened figures if there are any


class King(Figure):
    def __init__(self, index, color, white_positions, black_positions, position):
        super().__init__(index, color, white_positions, black_positions, position)

    def get_possible_movement_positions(self):
        return 1  # return all possible movement positions

    def check_threatenings(self):
        return 1  # return index of threatened figures if there are any


class Chessboard:

    def __init__(self):
        self.icon_dict = {}
        self.white_positions = np.squeeze(np.zeros((64, 1), dtype=np.uint8))
        self.black_positions = np.squeeze(np.zeros((64, 1), dtype=np.uint8))
        self.white_figures = []
        self.black_figures = []

    def initialize_standard_board(self):
        self.white_positions[0:16] = np.array(range(16)) + 1
        self.black_positions[48:64] = np.array(range(16)) + 17
        # set white figures
        # Pawns
        for i in range(8):  # create white pawns
            self.white_figures.append(Pawn(i + 9, 'white', self.white_positions, self.black_positions, i + 8))
        # Rooks
        self.white_figures.append(Rook(1, 'white', self.white_positions, self.black_positions, 0))
        self.white_figures.append(Rook(8, 'white', self.white_positions, self.black_positions, 7))
        # Knights
        self.white_figures.append(Knight(2, 'white', self.white_positions, self.black_positions, 1))
        self.white_figures.append(Knight(7, 'white', self.white_positions, self.black_positions, 6))
        # Bishops
        self.white_figures.append(Bishop(3, 'white', self.white_positions, self.black_positions, 2))
        self.white_figures.append(Bishop(6, 'white', self.white_positions, self.black_positions, 5))
        # King and Queen
        self.white_figures.append(King(4, 'white', self.white_positions, self.black_positions, 3))
        self.white_figures.append(Queen(5, 'white', self.white_positions, self.black_positions, 4))
        # set black figures
        # Pawns
        for i in range(8):  # create black pawns
            self.black_figures.append(Pawn(i + 17, 'black', self.white_positions, self.black_positions, i + 48))
        # Rooks
        self.black_figures.append(Rook(25, 'black', self.white_positions, self.black_positions, 56))
        self.black_figures.append(Rook(32, 'black', self.white_positions, self.black_positions, 63))
        # Knights
        self.black_figures.append(Knight(26, 'black', self.white_positions, self.black_positions, 57))
        self.black_figures.append(Knight(31, 'black', self.white_positions, self.black_positions, 62))
        # Bishops
        self.black_figures.append(Bishop(27, 'black', self.white_positions, self.black_positions, 58))
        self.black_figures.append(Bishop(30, 'black', self.white_positions, self.black_positions, 61))
        # King and Queen
        self.black_figures.append(King(28, 'black', self.white_positions, self.black_positions, 59))
        self.black_figures.append(Queen(29, 'black', self.white_positions, self.black_positions, 60))

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

        for figure in self.white_figures:
            # get figure image keys
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

        for figure in self.black_figures:
            # get figure image keys
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

    def get_all_possible_moves(self, color):
        if color == 'white':
            all_moves = []
            for figure in self.white_figures:
                all_moves.append(figure.get_possible_movement_positions())
            return moves
        else:
            A = 1
