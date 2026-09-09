import numpy as np

vagas = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1]
]

ocupadas = np.sum(vagas)
desocupadas = 9 - ocupadas

print("Há", desocupadas, "vagas desocupadas e", ocupadas, "vagas ocupadas.")