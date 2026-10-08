import numpy as np

temperaturas = []

for i in range(0,5):
    media_do_dia = float(input("Insira a média da temperatura do dia: "))
    temperaturas.append(media_do_dia)

media = sum(temperaturas)/5

if media >= 18 and media <=28:
    print("A média de temperatura está dentro da faixa ideal:",media, "C")
else:
    print("A média de temperatura não está dentro da faixa ideal:",media,"C")

print(temperaturas)