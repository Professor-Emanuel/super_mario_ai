import pygame
# from setari import ROSU
from utilitati.desen import deseneaza_obstacol


class Obstacol:
    def __init__(self, x, y, latime=40, inaltime=40):
        self.rect = pygame.Rect(x, y, latime, inaltime)

    def deseneaza(self, ecran):
        #pygame.draw.rect(ecran, ROSU, self.rect)
        deseneaza_obstacol(ecran, self.rect)