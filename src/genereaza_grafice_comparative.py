import csv
import os

import matplotlib.pyplot as plt


def citeste_csv(cale):
    episoade = []
    recompense = []
    succese = []

    with open(cale, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for rand in reader:
            episoade.append(int(rand["episod"]))
            recompense.append(float(rand["recompensa"]))
            succese.append(int(rand["succes"]))

    return episoade, recompense, succese


def medie_mobila(valori, fereastra=100):
    rezultat = []

    for i in range(len(valori)):
        start = max(0, i - fereastra + 1)
        subset = valori[start:i + 1]
        rezultat.append(sum(subset) / len(subset))

    return rezultat


def rata_succes_mobila(succese, fereastra=100):
    rezultat = []

    for i in range(len(succese)):
        start = max(0, i - fereastra + 1)
        subset = succese[start:i + 1]
        rezultat.append(sum(subset) / len(subset) * 100)

    return rezultat


def main():
    os.makedirs("rezultate/grafice", exist_ok=True)

    ep_random, recomp_random, succese_random = citeste_csv(
        "rezultate/random_rezultate.csv"
    )

    ep_q, recomp_q, succese_q = citeste_csv(
        "rezultate/q_learning_rezultate.csv"
    )

    plt.figure()
    plt.plot(ep_random, medie_mobila(recomp_random), label="Agent random")
    plt.plot(ep_q, medie_mobila(recomp_q), label="Q-learning")
    plt.xlabel("Episod")
    plt.ylabel("Recompensă medie mobilă")
    plt.title("Comparație recompensă: Random vs Q-learning")
    plt.legend()
    plt.grid(True)
    plt.savefig("rezultate/grafice/comparatie_recompensa.png")
    plt.close()

    plt.figure()
    plt.plot(ep_random, rata_succes_mobila(succese_random), label="Agent random")
    plt.plot(ep_q, rata_succes_mobila(succese_q), label="Q-learning")
    plt.xlabel("Episod")
    plt.ylabel("Rată de succes (%)")
    plt.title("Comparație rată de succes: Random vs Q-learning")
    plt.legend()
    plt.grid(True)
    plt.savefig("rezultate/grafice/comparatie_rata_succes.png")
    plt.close()

    print("Grafice comparative generate în rezultate/grafice/")


if __name__ == "__main__":
    main()