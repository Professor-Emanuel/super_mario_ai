import csv
import os

from mediu.platformer_env import PlatformerEnv
from ai.agent_q_learning import AgentQLearning


def ruleaza_episod(env, agent):
    stare = env.reset()
    done = False

    recompensa_totala = 0
    pasi = 0
    succes = False

    while not done:
        actiune = agent.alege_actiune(stare)
        stare_urmatoare, recompensa, done, info = env.step(actiune)

        agent.invata(stare, actiune, recompensa, stare_urmatoare, done)

        stare = stare_urmatoare
        recompensa_totala += recompensa
        pasi += 1

        if info.get("succes", False):
            succes = True

    agent.scade_epsilon()

    return recompensa_totala, pasi, succes


def antreneaza_nivel(nivel, numar_episoade=5000):
    print(f"\n=== Antrenare Q-learning pe nivelul {nivel} ===")

    os.makedirs("modele", exist_ok=True)
    os.makedirs("rezultate", exist_ok=True)

    env = PlatformerEnv(render=False, nivel=nivel)
    agent = AgentQLearning(numar_actiuni=5)

    recompense = []
    succese = 0
    istoric = []

    for episod in range(1, numar_episoade + 1):
        recompensa, pasi, succes = ruleaza_episod(env, agent)

        recompense.append(recompensa)

        if succes:
            succese += 1

        istoric.append({
            "nivel": nivel,
            "episod": episod,
            "recompensa": recompensa,
            "pasi": pasi,
            "succes": int(succes),
            "epsilon": agent.epsilon
        })

        if episod % 50 == 0:
            recompensa_medie_50 = sum(recompense[-50:]) / 50

            print(
                f"Nivel {nivel} | "
                f"Episod {episod:04d} | "
                f"Recompensa medie ultimele 50: {recompensa_medie_50:8.2f} | "
                f"Epsilon: {agent.epsilon:.3f} | "
                f"Succese totale: {succese}"
            )

    rata_succes = succese / numar_episoade * 100
    recompensa_medie = sum(recompense) / len(recompense)

    cale_model = f"modele/q_learning_nivel_{nivel}.pkl"
    cale_csv = f"rezultate/q_learning_nivel_{nivel}.csv"

    agent.salveaza(cale_model)

    with open(cale_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["nivel", "episod", "recompensa", "pasi", "succes", "epsilon"]
        )
        writer.writeheader()
        writer.writerows(istoric)

    print(f"\nRezultate nivel {nivel}:")
    print(f"Episoade: {numar_episoade}")
    print(f"Rata succes: {rata_succes:.2f}%")
    print(f"Recompensa medie: {recompensa_medie:.2f}")
    print(f"Dimensiune Q-table: {len(agent.q_table)} stari")
    print(f"Model salvat in {cale_model}")
    print(f"Rezultate salvate in {cale_csv}")

    env.inchide()


def main():
    for nivel in [1, 2, 3]:
        antreneaza_nivel(nivel=nivel, numar_episoade=5000)


if __name__ == "__main__":
    main()