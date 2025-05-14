#Bitboards?
import os

class Piece:
    def __init__(self, identity, color, value, texture=None, texture_rect=None):
        self.identity = identity 
        self.color = color
        value_a = 1 if color == 'white' else -1
        self.value = value * value_a
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self, size=80): 
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.identity}.png')
        
    def moves(self, move):
        pass

class Pawn(Piece):
    def __init__(self, color):
        self.direction = -1 if color == 'white' else 1
        super().__init__('pawn', color, 1.0)

class Knight(Piece):
    def __init__(self, color):
        super().__init__('knight', color, 3.0)

class Bishop(Piece):
    def __init__(self, color):
        super().__init__('bishop', color, 3.0)

class Rook(Piece):
    def __init__(self, color):
        super().__init__('rook', color, 5.0 )

class Queen(Piece):
    def __init__(self, color):
        super().__init__('queen', color, 9.0)
        
class King(Piece):
    def __init__(self, color):
        super().__init__('king', color, float('inf'))
