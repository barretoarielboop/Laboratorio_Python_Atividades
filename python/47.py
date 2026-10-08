import numpy as np

matriz = np.array([
    [1, 2],
    [3, 4]
])
positivos = []

for linha in matriz:
    for numero in linha:
        if numero > 0:
            positivos.append(numero)

total = len(positivos)

print(total)