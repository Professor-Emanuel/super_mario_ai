import random


class AgentRandom:
    def __init__(self, numar_actiuni):
        self.numar_actiuni = numar_actiuni

    def alege_actiune(self, stare):
        return random.randint(0, self.numar_actiuni - 1)