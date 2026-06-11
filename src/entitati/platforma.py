import pygame
#from setari import VERDE
from utilitati.desen import deseneaza_platforma


class Platforma:
    def __init__(self, x, y, latime, inaltime):
        self.rect = pygame.Rect(x, y, latime, inaltime)

    def deseneaza(self, ecran):
        #pygame.draw.rect(ecran, VERDE, self.rect)
        deseneaza_platforma(ecran, self.rect)

