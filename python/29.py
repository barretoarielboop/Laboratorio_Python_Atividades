import numpy as np

melhores_vendas = ()

for i in range(0, 5):
    vendas = float(input("Insira o lucro gerado pelo(a) vendedor(a):"))
    melhores_vendas.append(vendas)

maior_nota = np.max(melhores_vendas)

print(maior_nota)