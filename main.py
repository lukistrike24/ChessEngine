from time import time
from Classes import Chessboard
from lookup_tables import get_movement_LT_dict

Lookup_Tables = get_movement_LT_dict()

board = Chessboard()

board.initialize_standard_board(Lookup_Tables)

start = time()
board.make_random_moves(1000000, plot=True, plot_all=False)
print(time() - start)

# board.visualize_board()

# white_moves = board.get_all_possible_moves('white')
# black_moves = board.get_all_possible_moves('black')
#
# A = 1
#
# start = time()
# for i in range(10000):
#     white_moves = board.get_all_possible_moves('white')
#     black_moves = board.get_all_possible_moves('black')
# print(time()-start)
