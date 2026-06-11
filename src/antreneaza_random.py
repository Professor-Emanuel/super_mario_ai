import csv
import os

from mediu.platformer_env import PlatformerEnv
from ai.agent_random import AgentRandom


def ruleaza_episod(env, agent):
    stare = env.reset()
    done = False

    recompensa_totala = 0
    pasi = 0
    succes = False

    while not done:
        actiune = agent.alege_actiune(stare)
        stare, recompensa, info_done, info = env.step(actiune)

        done = info_done
        recompensa_totala += recompensa
        pasi += 1

        if env.jucator.rect.colliderect(env.finish):
            succes = True

    return recompensa_totala, pasi, succes


def main():
    os.makedirs("rezultate", exist_ok=True)

    env = PlatformerEnv(render=False)
    agent = AgentRandom(numar_actiuni=5)

    numar_episoade = 5000

    recompense = []
    succese = 0
    istoric = []

    for episod in range(1, numar_episoade + 1):
        recompensa, pasi, succes = ruleaza_episod(env, agent)

        recompense.append(recompensa)

        if succes:
            succese += 1

        istoric.append({
            "episod": episod,
            "recompensa": recompensa,
            "pasi": pasi,
            "succes": int(succes)
        })

        if episod % 50 == 0:
            ultimele_recompense = recompense[-50:]
            recompensa_medie_50 = sum(ultimele_recompense) / len(ultimele_recompense)

            print(
                f"Episod {episod:04d} | "
                f"Recompensa medie ultimele 50: {recompensa_medie_50:8.2f} | "
                f"Succese totale: {succese}"
            )

    rata_succes = succese / numar_episoade * 100
    recompensa_medie = sum(recompense) / len(recompense)

    print("\nRezultate agent random:")
    print(f"Episoade: {numar_episoade}")
    print(f"Rata succes: {rata_succes:.2f}%")
    print(f"Recompensa medie: {recompensa_medie:.2f}")

    with open("rezultate/random_rezultate.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["episod", "recompensa", "pasi", "succes"]
        )
        writer.writeheader()
        writer.writerows(istoric)

    print("Rezultatele au fost salvate in rezultate/random_rezultate.csv")

    env.inchide()


if __name__ == "__main__":
    main()