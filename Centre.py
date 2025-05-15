import sys
import pygame
from constants import *
from active import Active
from Control import Control

class Centre:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('CHESS')
        self.active = Active()
        self.control = Control(self.active)

    def centreloop(self):
        while True:
            self.active.background(self.screen)
            self.active.display_pieces(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        row = y // SQRSIZE
                        col = x // SQRSIZE
                        self.control.handling(row, col)
                        print({row},{col})
            pygame.display.update()

centre = Centre()
centre.centreloop()