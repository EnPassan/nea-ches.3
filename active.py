import pygame
from constants import *
from Board import Board

class Active:
    def __init__(self):
        self.board = Board()

    def background(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88)
                
                rect = (row * SQRSIZE, col * SQRSIZE, SQRSIZE, SQRSIZE)

                pygame.draw.rect(surface, color, rect)
    
    def display_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].contains_piece():
                    piece = self.board.squares[row][col].piece

                    img = pygame.image.load(piece.texture)
                    img_center = col * SQRSIZE + SQRSIZE // 2, row * SQRSIZE + SQRSIZE // 2
                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)
