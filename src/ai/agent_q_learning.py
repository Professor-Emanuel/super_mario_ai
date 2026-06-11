import random
import numpy as np
import pickle

class AgentQLearning:
    def __init__(
        self,
        numar_actiuni,
        rata_invatare=0.1,
        gamma=0.95,
        epsilon=1.0,
        epsilon_min=0.05,
        epsilon_decay=0.999
    ):
        self.numar_actiuni = numar_actiuni

        self.rata_invatare = rata_invatare
        self.gamma = gamma

        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay

        self.q_table = {}

    def discretizeaza_stare(self, stare):
        x, y, vx, vy, dist_finish, dist_obstacol, pe_sol = stare

        return (
            int(x // 50),
            int(y // 50),
            int(vx),
            int(vy // 5),
            int(dist_finish // 50),
            int(dist_obstacol // 50),
            int(pe_sol)
        )

    def obtine_q_values(self, stare_discreta):
        if stare_discreta not in self.q_table:
            self.q_table[stare_discreta] = np.zeros(self.numar_actiuni)

        return self.q_table[stare_discreta]

    def alege_actiune(self, stare):
        stare_discreta = self.discretizeaza_stare(stare)

        if random.random() < self.epsilon:
            return random.randint(0, self.numar_actiuni - 1)

        q_values = self.obtine_q_values(stare_discreta)
        return int(np.argmax(q_values))

    def invata(self, stare, actiune, recompensa, stare_urmatoare, done):
        stare_discreta = self.discretizeaza_stare(stare)
        stare_urmatoare_discreta = self.discretizeaza_stare(stare_urmatoare)

        q_values = self.obtine_q_values(stare_discreta)
        q_urmator = self.obtine_q_values(stare_urmatoare_discreta)

        q_curent = q_values[actiune]

        if done:
            tinta = recompensa
        else:
            tinta = recompensa + self.gamma * np.max(q_urmator)

        q_values[actiune] = q_curent + self.rata_invatare * (tinta - q_curent)

    def scade_epsilon(self):
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def salveaza(self, cale_fisier):
        with open(cale_fisier, "wb") as f:
            pickle.dump(self.q_table, f)

    def incarca(self, cale_fisier):
        with open(cale_fisier, "rb") as f:
            self.q_table = pickle.load(f)