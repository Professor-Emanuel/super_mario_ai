from mediu.platformer_env import PlatformerEnv
from ai.agent_random import AgentRandom


def main():
    env = PlatformerEnv(render=True)
    agent = AgentRandom(numar_actiuni=5)

    stare = env.reset()
    done = False

    while not done:
        actiune = agent.alege_actiune(stare)
        stare, recompensa, done, info = env.step(actiune)

    env.inchide()


if __name__ == "__main__":
    main()