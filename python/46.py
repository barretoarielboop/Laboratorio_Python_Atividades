import numpy as np

matriz = np.array([
    [1, 2],
    [3, 4]
])

diagonal = np.diagonal(matriz)
soma = np.sum(diagonal)

print(diagonal)
print(soma)