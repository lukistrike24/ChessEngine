
from Classes import Chessboard
from lookup_tables import get_movement_LT_dict

Lookup_Tables = get_movement_LT_dict()

board = Chessboard()

board.initialize_standard_board(Lookup_Tables)

board.visualize_board()

board.get_all_possible_moves('white')

