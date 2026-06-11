from mediu.platformer_env import PlatformerEnv
from ai.agent_q_learning import AgentQLearning
import csv


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

        if env.jucator.rect.colliderect(env.finish):
            succes = True

    agent.scade_epsilon()

    return recompensa_totala, pasi, succes


def main():
    env = PlatformerEnv(render=False)
    agent = AgentQLearning(numar_actiuni=5)

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
            "succes": int(succes),
            "epsilon": agent.epsilon
        })

        if episod % 50 == 0:
            ultimele_recompense = recompense[-50:]
            recompensa_medie = sum(ultimele_recompense) / len(ultimele_recompense)

            print(
                f"Episod {episod:04d} | "
                f"Recompensa medie ultimele 50: {recompensa_medie:8.2f} | "
                f"Epsilon: {agent.epsilon:.3f} | "
                f"Succese totale: {succese}"
            )


    rata_succes = succese / numar_episoade * 100
    recompensa_medie = sum(recompense) / len(recompense)

    print("\nRezultate Q-learning:")
    print(f"Episoade: {numar_episoade}")
    print(f"Rata succes: {rata_succes:.2f}%")
    print(f"Recompensa medie: {recompensa_medie:.2f}")
    print(f"Dimensiune Q-table: {len(agent.q_table)} stari")
    agent.salveaza("modele/q_learning.pkl")
    print("Model salvat in modele/q_learning.pkl")

    with open("rezultate/q_learning_rezultate.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["episod", "recompensa", "pasi", "succes", "epsilon"]
        )
        writer.writeheader()
        writer.writerows(istoric)

    print("Rezultatele au fost salvate in rezultate/q_learning_rezultate.csv")

    env.inchide()


if __name__ == "__main__":
    main()