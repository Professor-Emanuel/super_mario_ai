import pygame
from setari import VITEZA_JUCATOR, PUTERE_SARITURA, GRAVITATIE
from utilitati.desen import deseneaza_jucator

class Jucator:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 50)
        self.vx = 0
        self.vy = 0
        self.pe_sol = False

    def aplica_actiune(self, actiune):
        self.vx = 0

        if actiune == 1:      # stanga
            self.vx = -VITEZA_JUCATOR
        elif actiune == 2:    # dreapta
            self.vx = VITEZA_JUCATOR
        elif actiune == 3:    # sari
            self.sari()
        elif actiune == 4:    # dreapta + sari
            self.vx = VITEZA_JUCATOR
            self.sari()

    def sari(self):
        if self.pe_sol:
            self.vy = PUTERE_SARITURA
            self.pe_sol = False

    def update(self, platforme):
        self.vy += GRAVITATIE

        self.rect.x += self.vx
        self.verifica_coliziuni_x(platforme)

        self.rect.y += self.vy
        self.pe_sol = False
        self.verifica_coliziuni_y(platforme)

    def verifica_coliziuni_x(self, platforme):
        for platforma in platforme:
            if self.rect.colliderect(platforma.rect):
                if self.vx > 0:
                    self.rect.right = platforma.rect.left
                elif self.vx < 0:
                    self.rect.left = platforma.rect.right

    def verifica_coliziuni_y(self, platforme):
        for platforma in platforme:
            if self.rect.colliderect(platforma.rect):
                if self.vy > 0:
                    self.rect.bottom = platforma.rect.top
                    self.vy = 0
                    self.pe_sol = True
                elif self.vy < 0:
                    self.rect.top = platforma.rect.bottom
                    self.vy = 0

    def deseneaza(self, ecran):
        deseneaza_jucator(ecran, self.rect, self.vx)
