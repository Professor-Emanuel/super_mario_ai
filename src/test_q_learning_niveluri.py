from mediu.platformer_env import PlatformerEnv
from ai.agent_q_learning import AgentQLearning


def testeaza_model(nivel):
    print(f"\n=== Testare nivel {nivel} ===")

    env = PlatformerEnv(render=True, nivel=nivel)
    agent = AgentQLearning(numar_actiuni=5)

    agent.incarca(f"modele/q_learning_nivel_{nivel}.pkl")

    agent.epsilon = 0.0

    stare = env.reset()
    done = False

    recompensa_totala = 0

    while not done:
        actiune = agent.alege_actiune(stare)  # epsilon e mic -> greedy
        stare, recompensa, done, info = env.step(actiune)

        recompensa_totala += recompensa

    print(f"Recompensa totală: {recompensa_totala:.2f}")
    print(f"Succes: {info.get('succes', False)}")

    env.inchide()


def main():
    for nivel in [1, 2, 3]:
        testeaza_model(nivel)


if __name__ == "__main__":
    main()