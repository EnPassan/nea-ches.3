import pygame, sys
from constants import *

class Control:
    def __init__(self, active):
        self.active = active 
        self.selected = None

    def handling(self, row, col):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    row = y // SQRSIZE
                    col = x // SQRSIZE
                   

    