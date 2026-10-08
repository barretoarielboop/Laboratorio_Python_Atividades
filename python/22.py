import numpy as np

notas = []

for i in range(0, 5):
    produto = float(input("Insira as notas dos estudantes:"))
    notas.append(produto)

maior_nota = np.max(notas)

print(maior_nota)