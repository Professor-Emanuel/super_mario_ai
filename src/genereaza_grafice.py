import csv
import os

import matplotlib.pyplot as plt


def citeste_rezultate(cale_fisier):
    episoade = []
    recompense = []
    succese = []

    with open(cale_fisier, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for rand in reader:
            episoade.append(int(rand["episod"]))
            recompense.append(float(rand["recompensa"]))
            succese.append(int(rand["succes"]))

    return episoade, recompense, succese


def medie_mobila(valori, fereastra=100):
    medii = []

    for i in range(len(valori)):
        start = max(0, i - fereastra + 1)
        subset = valori[start:i + 1]
        medii.append(sum(subset) / len(subset))

    return medii


def rata_succes_mobila(succese, fereastra=100):
    rate = []

    for i in range(len(succese)):
        start = max(0, i - fereastra + 1)
        subset = succese[start:i + 1]
        rate.append(sum(subset) / len(subset) * 100)

    return rate


def main():
    os.makedirs("rezultate/grafice", exist_ok=True)

    episoade, recompense, succese = citeste_rezultate(
        "rezultate/q_learning_rezultate.csv"
    )

    recompensa_medie = medie_mobila(recompense, fereastra=100)
    rata_succes = rata_succes_mobila(succese, fereastra=100)

    plt.figure()
    plt.plot(episoade, recompensa_medie)
    plt.xlabel("Episod")
    plt.ylabel("Recompensă medie mobilă")
    plt.title("Evoluția recompensei în timpul antrenării")
    plt.grid(True)
    plt.savefig("rezultate/grafice/recompensa_q_learning.png")
    plt.close()

    plt.figure()
    plt.plot(episoade, rata_succes)
    plt.xlabel("Episod")
    plt.ylabel("Rată de succes (%)")
    plt.title("Evoluția ratei de succes în timpul antrenării")
    plt.grid(True)
    plt.savefig("rezultate/grafice/rata_succes_q_learning.png")
    plt.close()

    print("Grafice generate în rezultate/grafice/")


if __name__ == "__main__":
    main()