from constants import *
from Square import Square
from Piece import *


class Board:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self._create()
        self._pieces('white')
        self._pieces('black')

    def _create(self):#private-->(_)
        for row in range(ROWS):
            for col in range (COLS):
                self.squares[row][col] = Square(row, col)
                
        #use bitboards
        #def print_bitboard(bb):
          #  for rank in range(7, -1, -1):
           #     for file in range(8):
            #        index = rank * 8 + file
             #       print('1' if (bb >> index) & 1 else '.', end=' ')
              #  print()
            #print()

    def _pieces(self, color):#private-->(_)
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)
        
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        self.squares[row_other][4] = Square(row_other, 4, King(color))

        self.squares[row_other][3] = Square(row_other, 3, Queen(color))