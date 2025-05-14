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
                    
            pygame.display.update()

centre = Centre()
centre.centreloop()