import numpy as np

tabuleiro = np.zeros((8,8), dtype=int)

valor = 1

for i in range(8):
    for j in range(8):
        tabuleiro[i][j] = valor
        valor * 2

print(tabuleiro)