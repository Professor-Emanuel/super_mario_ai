import csv
import os


def citeste_csv(cale):
    recompense = []
    succese = []
    pasi = []

    with open(cale, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for rand in reader:
            recompense.append(float(rand["recompensa"]))
            succese.append(int(rand["succes"]))
            pasi.append(int(rand["pasi"]))

    return recompense, succese, pasi


def calculeaza_statistici(nivel):
    cale = f"rezultate/q_learning_nivel_{nivel}.csv"

    recompense, succese, pasi = citeste_csv(cale)

    episoade = len(recompense)
    rata_succes = sum(succese) / episoade * 100
    recompensa_medie = sum(recompense) / episoade
    pasi_medii = sum(pasi) / episoade

    return {
        "nivel": nivel,
        "episoade": episoade,
        "rata_succes": rata_succes,
        "recompensa_medie": recompensa_medie,
        "pasi_medii": pasi_medii,
    }


def genereaza_latex(statistici):
    linii = []

    linii.append("\\begin{table}[H]")
    linii.append("\\centering")
    linii.append("\\begin{tabular}{|c|c|c|c|c|}")
    linii.append("\\hline")
    linii.append("\\textbf{Nivel} & \\textbf{Episoade} & \\textbf{Rată succes} & \\textbf{Recompensă medie} & \\textbf{Pași medii} \\\\")
    linii.append("\\hline")

    for stat in statistici:
        linii.append(
            f"{stat['nivel']} & "
            f"{stat['episoade']} & "
            f"{stat['rata_succes']:.2f}\\% & "
            f"{stat['recompensa_medie']:.2f} & "
            f"{stat['pasi_medii']:.2f} \\\\"
        )
        linii.append("\\hline")

    linii.append("\\end{tabular}")
    linii.append("\\caption{Performanța agentului Q-learning pe niveluri diferite}")
    linii.append("\\label{tab:performanta-niveluri}")
    linii.append("\\end{table}")

    return "\n".join(linii)


def main():
    os.makedirs("rezultate/tabele", exist_ok=True)

    statistici = []

    for nivel in [1, 2, 3]:
        statistici.append(calculeaza_statistici(nivel))

    latex = genereaza_latex(statistici)

    cale_output = "rezultate/tabele/tabel_performanta_niveluri.tex"

    with open(cale_output, "w", encoding="utf-8") as f:
        f.write(latex)

    print("Tabel LaTeX generat:")
    print(cale_output)
    print()
    print(latex)


if __name__ == "__main__":
    main()