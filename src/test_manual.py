import pygame

from mediu.platformer_env import PlatformerEnv


def citeste_actiune_tastatura():
    taste = pygame.key.get_pressed()

    # D + W = dreapta + saritura
    if taste[pygame.K_d] and taste[pygame.K_w]:
        return 4  # dreapta + saritura

    # A = stanga
    if taste[pygame.K_a]:
        return 1  # stanga

    # D = dreapta
    if taste[pygame.K_d]:
        return 2  # dreapta

    # W = saritura (doar daca nu e combinat cu D)
    if taste[pygame.K_w]:
        return 3  # saritura

    return 0  # nimic

def main():
    env = PlatformerEnv(render=True, nivel=1)
    stare = env.reset()
    done = False
    recompensa_totala = 0

    while not done:
        actiune = citeste_actiune_tastatura()
        stare, recompensa, done, info = env.step(actiune)
        recompensa_totala += recompensa

    print(f"Episod terminat. Recompensa totala: {recompensa_totala:.2f}")
    env.inchide()


if __name__ == "__main__":
    main()