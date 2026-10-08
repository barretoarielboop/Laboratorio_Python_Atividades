import numpy as np

conjunto = []

for i in range(0, 3):
    gastos = float(input("Insira os valores gastos no mês:"))
    conjunto.append(gastos)

soma = np.sum(conjunto)

print(soma)