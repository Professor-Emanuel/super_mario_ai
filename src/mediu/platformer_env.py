import pygame
import numpy as np

from setari import LATIME_ECRAN, INALTIME_ECRAN
from entitati.jucator import Jucator
from entitati.platforma import Platforma
from entitati.obstacol import Obstacol
from utilitati.desen import deseneaza_background, deseneaza_finish


class PlatformerEnv:
    def __init__(self, render=True, nivel=1):
        self.render_activ = render
        self.nivel = nivel

        if self.render_activ:
            pygame.init()
            self.ecran = pygame.display.set_mode((LATIME_ECRAN, INALTIME_ECRAN))
            pygame.display.set_caption(f"Mini Platformer RL - Nivel {nivel}")
            self.ceas = pygame.time.Clock()

        self.reset()

    def reset(self):
        self.jucator = Jucator(80, 350)

        if self.nivel == 1:
            self.platforme = [
                Platforma(0, 450, 1200, 50),
                Platforma(250, 370, 140, 20),
                Platforma(500, 320, 140, 20),
            ]

            self.obstacole = [
                Obstacol(420, 410),
                Obstacol(700, 410),
            ]

            self.finish = pygame.Rect(820, 390, 40, 60)

        elif self.nivel == 2:
            self.platforme = [
                Platforma(0, 450, 1300, 50),
                Platforma(230, 380, 120, 20),
                Platforma(430, 330, 120, 20),
                Platforma(650, 360, 120, 20),
            ]

            self.obstacole = [
                Obstacol(360, 410),
                Obstacol(560, 410),
                Obstacol(760, 410),
            ]

            self.finish = pygame.Rect(850, 390, 40, 60)

        elif self.nivel == 3:
            self.platforme = [
                Platforma(0, 450, 1400, 50),
                Platforma(190, 380, 100, 20),
                Platforma(370, 320, 110, 20),
                Platforma(570, 370, 110, 20),
                Platforma(740, 300, 110, 20),
            ]

            self.obstacole = [
                Obstacol(310, 410),
                Obstacol(500, 410),
                Obstacol(680, 410),
                Obstacol(820, 410),
            ]

            self.finish = pygame.Rect(850, 240, 40, 60)

        else:
            raise ValueError("Nivel invalid. Alege nivel=1, nivel=2 sau nivel=3.")

        self.pas_curent = 0
        self.max_pasi = 1800
        self.x_anterior = self.jucator.rect.x

        return self.get_state()

    def step(self, actiune):
        self.pas_curent += 1

        self.jucator.aplica_actiune(actiune)
        self.jucator.update(self.platforme)

        reward = self.calculeaza_recompensa()
        done = self.verifica_done()

        state = self.get_state()
        info = {
            "nivel": self.nivel,
            "succes": self.jucator.rect.colliderect(self.finish)
        }

        if self.render_activ:
            self.render()

        return state, reward, done, info

    def get_state(self):
        distanta_finish = self.finish.x - self.jucator.rect.x

        obstacol_apropiat = min(
            self.obstacole,
            key=lambda obstacol: abs(obstacol.rect.x - self.jucator.rect.x)
        )

        distanta_obstacol = obstacol_apropiat.rect.x - self.jucator.rect.x

        return np.array([
            self.jucator.rect.x,
            self.jucator.rect.y,
            self.jucator.vx,
            self.jucator.vy,
            distanta_finish,
            distanta_obstacol,
            int(self.jucator.pe_sol)
        ], dtype=np.float32)

    def calculeaza_recompensa(self):
        reward = 0

        progres = self.jucator.rect.x - self.x_anterior
        reward += progres * 0.3
        self.x_anterior = self.jucator.rect.x

        reward -= 0.05

        for obstacol in self.obstacole:
            if self.jucator.rect.colliderect(obstacol.rect):
                reward -= 50

        if self.jucator.rect.colliderect(self.finish):
            reward += 100

        if self.jucator.rect.y > INALTIME_ECRAN:
            reward -= 50

        return reward

    def verifica_done(self):
        if self.jucator.rect.colliderect(self.finish):
            return True

        if self.jucator.rect.y > INALTIME_ECRAN:
            return True

        for obstacol in self.obstacole:
            if self.jucator.rect.colliderect(obstacol.rect):
                return True

        if self.pas_curent >= self.max_pasi:
            return True

        return False

    def render(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        deseneaza_background(self.ecran)

        for platforma in self.platforme:
            platforma.deseneaza(self.ecran)

        for obstacol in self.obstacole:
            obstacol.deseneaza(self.ecran)

        deseneaza_finish(self.ecran, self.finish)
        self.jucator.deseneaza(self.ecran)

        pygame.display.flip()
        self.ceas.tick(60)

    def inchide(self):
        if self.render_activ:
            pygame.quit()