import numpy as np
from . import Pawn
class Chessboard():
    def __init__(self):
        self.board = np.zeros((8,8), dtype=int)
        self.init_pawns()
    
    def color_tiles(self):
        for col in range(8):
            for row in range(8):
                if (col+row)%2 == 0:
                    self.board[col][row] = 1

    def init_pawns(self):
        for col in range(8):
            self.board[1][col] = 'P'

    def pboard(self):
        print(self.board)
    
cb = Chessboard()
#cb.add_items()
cb.pboard()