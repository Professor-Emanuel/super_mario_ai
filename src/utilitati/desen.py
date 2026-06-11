import pygame
import math

from setari import (
    LATIME_ECRAN,
    INALTIME_ECRAN,
    ALB,
    NEGRU,
    ALBASTRU,
    VERDE,
    ROSU,
    GALBEN,
)


CER = (135, 206, 235)
CER_SUS = (92, 170, 235)
NOR = (245, 245, 245)
IARBA = (70, 200, 90)
PAMANT = (130, 82, 45)
PAMANT_INCHIS = (95, 60, 35)
PIELE = (255, 210, 160)
MARO = (110, 70, 35)
PORTOCALIU = (240, 150, 50)
GRI = (110, 110, 120)
GRI_INCHIS = (70, 70, 80)
ALB_STEAG = (250, 250, 250)


def deseneaza_background(ecran):
    # Cer
    ecran.fill(CER)

    # Soare
    pygame.draw.circle(ecran, (255, 230, 90), (760, 90), 45)

    # Nori
    deseneaza_nor(ecran, 140, 90)
    deseneaza_nor(ecran, 420, 70)
    deseneaza_nor(ecran, 650, 140)

    # Dealuri fundal
    pygame.draw.circle(ecran, (95, 190, 110), (150, 470), 170)
    pygame.draw.circle(ecran, (80, 170, 100), (430, 490), 210)
    pygame.draw.circle(ecran, (100, 200, 120), (740, 470), 160)

    # Linie sol vizuală
    pygame.draw.rect(ecran, (110, 200, 90), (0, 440, LATIME_ECRAN, 60))


def deseneaza_nor(ecran, x, y):
    pygame.draw.circle(ecran, NOR, (x, y), 24)
    pygame.draw.circle(ecran, NOR, (x + 25, y - 10), 30)
    pygame.draw.circle(ecran, NOR, (x + 55, y), 24)
    pygame.draw.rect(ecran, NOR, (x, y, 55, 22), border_radius=12)


def deseneaza_platforma(ecran, rect):
    # Corp pământ
    pygame.draw.rect(ecran, PAMANT, rect, border_radius=5)

    # Iarbă deasupra
    iarba_rect = pygame.Rect(rect.x, rect.y, rect.width, 10)
    pygame.draw.rect(ecran, IARBA, iarba_rect, border_radius=5)

    # Textură pământ
    for x in range(rect.x + 10, rect.right, 28):
        pygame.draw.line(ecran, PAMANT_INCHIS, (x, rect.y + 18), (x + 12, rect.y + 30), 2)


def deseneaza_jucator(ecran, rect, vx=0):
    # Corp
    corp = pygame.Rect(rect.x + 8, rect.y + 18, 24, 28)
    pygame.draw.rect(ecran, ALBASTRU, corp, border_radius=6)

    # Cap
    pygame.draw.circle(ecran, PIELE, (rect.centerx, rect.y + 12), 12)

    # Șapcă
    sapca = pygame.Rect(rect.x + 8, rect.y + 1, 25, 10)
    pygame.draw.rect(ecran, PORTOCALIU, sapca, border_radius=5)
    pygame.draw.rect(ecran, PORTOCALIU, (rect.x + 25, rect.y + 7, 12, 5), border_radius=3)

    # Ochi
    pygame.draw.circle(ecran, NEGRU, (rect.centerx + 4, rect.y + 10), 2)

    # Picioare
    pygame.draw.rect(ecran, MARO, (rect.x + 8, rect.y + 43, 9, 7), border_radius=3)
    pygame.draw.rect(ecran, MARO, (rect.x + 23, rect.y + 43, 9, 7), border_radius=3)

    # Braț
    if vx >= 0:
        pygame.draw.line(ecran, PIELE, (rect.x + 30, rect.y + 25), (rect.x + 38, rect.y + 34), 4)
    else:
        pygame.draw.line(ecran, PIELE, (rect.x + 10, rect.y + 25), (rect.x + 2, rect.y + 34), 4)


def deseneaza_obstacol(ecran, rect):
    # Țepușă / spike
    puncte = [
        (rect.centerx, rect.y),
        (rect.right, rect.bottom),
        (rect.left, rect.bottom),
    ]
    pygame.draw.polygon(ecran, GRI_INCHIS, puncte)
    pygame.draw.polygon(ecran, GRI, [
        (rect.centerx, rect.y + 8),
        (rect.right - 8, rect.bottom - 4),
        (rect.left + 8, rect.bottom - 4),
    ])

    # Contur
    pygame.draw.polygon(ecran, NEGRU, puncte, width=2)


def deseneaza_finish(ecran, rect):
    # Stâlp
    pygame.draw.rect(ecran, NEGRU, (rect.x + 5, rect.y, 5, rect.height))

    # Steag
    steag = [
        (rect.x + 10, rect.y + 5),
        (rect.x + 42, rect.y + 15),
        (rect.x + 10, rect.y + 28),
    ]
    pygame.draw.polygon(ecran, GALBEN, steag)
    pygame.draw.polygon(ecran, NEGRU, steag, width=2)

    # Bază
    pygame.draw.rect(ecran, NEGRU, (rect.x - 4, rect.bottom - 5, 22, 5))