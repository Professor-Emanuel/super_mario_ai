# Mini Platformer RL

Proiect dezvoltat pentru lucrarea de licență **Reinforcement Learning**, având ca scop implementarea și evaluarea unui agent Q-learning într-un mediu de joc 2D de tip platformer.

Agentul controlează un personaj care trebuie să parcurgă un nivel, să evite obstacolele și să ajungă la zona finală. Comportamentul agentului este învățat prin interacțiune repetată cu mediul, pe baza recompenselor și penalizărilor primite.

---

## Echipa de proiect

- **Coordonator:** Dr. Emanuel-Attila Kőkővics
- **Student:** Vasile Gheorghe Vior

---

## Tehnologii utilizate

- **Python** - limbajul principal de implementare
- **Pygame** - construirea și randarea mediului de joc 2D
- **NumPy** - reprezentarea numerică a stărilor și valorilor Q
- **Matplotlib** - generarea graficelor experimentale
- **CSV** - salvarea rezultatelor obținute în timpul antrenării
- **pickle** - salvarea și încărcarea modelelor antrenate

---

## Structura proiectului

```text
super_mario_ai/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── modele/
│   ├── q_learning.pkl
│   ├── q_learning_nivel_1.pkl
│   ├── q_learning_nivel_2.pkl
│   └── q_learning_nivel_3.pkl
│
├── rezultate/
│   ├── grafice/
│   ├── tabele/
│   ├── random_rezultate.csv
│   ├── q_learning_rezultate.csv
│   ├── q_learning_nivel_1.csv
│   ├── q_learning_nivel_2.csv
│   └── q_learning_nivel_3.csv
│
└── src/
    ├── ai/
    │   ├── agent_random.py
    │   └── agent_q_learning.py
    │
    ├── entitati/
    │   ├── jucator.py
    │   ├── platforma.py
    │   └── obstacol.py
    │
    ├── mediu/
    │   └── platformer_env.py
    │
    ├── utilitati/
    │   └── desen.py
    │
    ├── antreneaza_random.py
    ├── antreneaza_q_learning.py
    ├── antreneaza_q_learning_niveluri.py
    ├── test_manual.py
    ├── test_q_learning.py
    ├── test_q_learning_niveluri.py
    ├── genereaza_grafice.py
    ├── genereaza_grafice_comparative.py
    ├── grafice_niveluri.py
    ├── genereaza_tabel_niveluri.py
    ├── main.py
    └── setari.py
```

---

## Descrierea mediului

Mediul implementat este un joc 2D de tip platformer. Acesta conține:

- un jucător controlat de agent;
- platforme pe care agentul se poate deplasa;
- obstacole care trebuie evitate;
- o zonă finală care marchează succesul episodului;
- mai multe niveluri cu dificultate crescătoare.

Mediul oferă două metode esențiale pentru Reinforcement Learning:

- `reset()` - reinițializează mediul și returnează starea inițială;
- `step(actiune)` - aplică acțiunea agentului și returnează noua stare, recompensa, condiția de terminare și informații suplimentare.

---

## Modelarea problemei

Problema este formulată ca un proces decizional Markov:

```text
(S, A, P, R, gamma)
```

unde:

- `S` reprezintă mulțimea stărilor;
- `A` reprezintă mulțimea acțiunilor;
- `P` reprezintă tranzițiile generate de regulile jocului;
- `R` reprezintă funcția de recompensă;
- `gamma` reprezintă factorul de discount.

Starea agentului este reprezentată printr-un vector numeric:

```text
[x, y, vx, vy, distanta_finish, distanta_obstacol, pe_sol]
```

Acțiunile disponibile sunt:

| Acțiune | Semnificație |
|---:|---|
| 0 | Nicio acțiune |
| 1 | Deplasare la stânga |
| 2 | Deplasare la dreapta |
| 3 | Săritură |
| 4 | Deplasare la dreapta + săritură |

---

## Agenți implementați

### Agent random

Agentul random alege acțiuni aleatorii și nu învață din experiență. Acesta este folosit ca metodă de referință pentru comparația cu agentul Q-learning.

### Agent Q-learning

Agentul Q-learning folosește o tabelă Q pentru a estima valoarea fiecărei acțiuni într-o stare discretizată. Acesta utilizează strategia `epsilon-greedy`, combinând explorarea cu exploatarea informației deja învățate.

Regula de actualizare utilizată este:

```text
Q(s,a) <- Q(s,a) + alpha * [r + gamma * max Q(s',a') - Q(s,a)]
```

---

## Instalare

Instalează dependențele proiectului folosind:

```bash
pip install -r requirements.txt
```

---

## Rulare

Comenzile se execută din directorul principal al proiectului.

### Testare manuală

Permite controlul manual al jucătorului cu tastele `A`, `D` și `W`.

```bash
python src/test_manual.py
```

### Antrenarea agentului random

```bash
python src/antreneaza_random.py
```

Rezultatele sunt salvate în:

```text
rezultate/random_rezultate.csv
```

### Antrenarea agentului Q-learning pe un nivel

```bash
python src/antreneaza_q_learning.py
```

Modelul și rezultatele sunt salvate în:

```text
modele/q_learning.pkl
rezultate/q_learning_rezultate.csv
```

### Antrenarea agentului Q-learning pe mai multe niveluri

```bash
python src/antreneaza_q_learning_niveluri.py
```

Modelele și rezultatele sunt salvate separat pentru fiecare nivel:

```text
modele/q_learning_nivel_1.pkl
modele/q_learning_nivel_2.pkl
modele/q_learning_nivel_3.pkl

rezultate/q_learning_nivel_1.csv
rezultate/q_learning_nivel_2.csv
rezultate/q_learning_nivel_3.csv
```

### Testarea vizuală a modelului Q-learning

```bash
python src/test_q_learning.py
```

### Testarea vizuală pe niveluri

```bash
python src/test_q_learning_niveluri.py
```

---

## Generarea graficelor

Pentru generarea graficelor de performanță se pot rula următoarele scripturi:

```bash
python src/genereaza_grafice.py
python src/genereaza_grafice_comparative.py
python src/grafice_niveluri.py
python src/genereaza_tabel_niveluri.py
```

Graficele generate sunt salvate în:

```text
rezultate/grafice/
```

Tabelele generate sunt salvate în:

```text
rezultate/tabele/
```

---

## Rezultate urmărite

În timpul experimentelor sunt urmărite următoarele valori:

- recompensa totală pe episod;
- numărul de pași executați;
- succesul sau eșecul episodului;
- rata de succes;
- recompensa medie;
- evoluția parametrului `epsilon` în timpul antrenării;
- dimensiunea tabelei Q.

Aceste rezultate sunt utilizate pentru compararea comportamentului agentului random cu agentul Q-learning și pentru evaluarea performanței pe niveluri diferite.

---

## Limitări

Implementarea folosește Q-learning tabular, ceea ce presupune discretizarea stărilor. Această abordare este potrivită pentru un mediu simplificat, dar poate deveni dificil de extins la medii mai complexe, cu spații de stare foarte mari sau observații vizuale complete.

O direcție viitoare de dezvoltare este înlocuirea tabelei Q cu o rețea neuronală, prin implementarea unui algoritm de tip Deep Q-Network.

---

## Autor

Proiect dezvoltat pentru lucrarea de licență.

**Student:** Vasile Gheorghe Vior  
**Coordonator:** Dr. Emanuel-Attila Kőkővics
