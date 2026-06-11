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

    plt.figure()

    for nivel in [1, 2, 3]:
        episoade, recompense, succese = citeste_csv(
            f"rezultate/q_learning_nivel_{nivel}.csv"
        )

        plt.plot(
            episoade,
            medie_mobila(recompense, fereastra=100),
            label=f"Nivel {nivel}"
        )

    plt.xlabel("Episod")
    plt.ylabel("Recompensă medie mobilă")
    plt.title("Comparație recompensă Q-learning pe niveluri")
    plt.legend()
    plt.grid(True)
    plt.savefig("rezultate/grafice/comparatie_recompensa_niveluri.png")
    plt.close()

    plt.figure()

    for nivel in [1, 2, 3]:
        episoade, recompense, succese = citeste_csv(
            f"rezultate/q_learning_nivel_{nivel}.csv"
        )

        plt.plot(
            episoade,
            rata_succes_mobila(succese, fereastra=100),
            label=f"Nivel {nivel}"
        )

    plt.xlabel("Episod")
    plt.ylabel("Rată de succes (%)")
    plt.title("Comparație rată succes Q-learning pe niveluri")
    plt.legend()
    plt.grid(True)
    plt.savefig("rezultate/grafice/comparatie_succes_niveluri.png")
    plt.close()

    print("Grafice comparative pe niveluri generate în rezultate/grafice/")


if __name__ == "__main__":
    main()