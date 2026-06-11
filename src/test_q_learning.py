from mediu.platformer_env import PlatformerEnv
from ai.agent_q_learning import AgentQLearning


def main():
    env = PlatformerEnv(render=True, nivel=1)

    agent = AgentQLearning(numar_actiuni=5)
    agent.incarca("modele/q_learning.pkl")
    agent.epsilon = 0.0

    stare = env.reset()
    done = False
    recompensa_totala = 0

    while not done:
        actiune = agent.alege_actiune(stare)
        stare, recompensa, done, info = env.step(actiune)
        recompensa_totala += recompensa

    print(f"Test terminat. Recompensa totala: {recompensa_totala:.2f}")
    env.inchide()


if __name__ == "__main__":
    main()