import random

numero_gerado = random.randint(1, 100)
aposta = int(input("Adivinhe o número gerado(1-100): "))

if aposta > numero_gerado:
    print("A sua aposta é maior do que o número sorteado.")
elif aposta < numero_gerado:
    print("A sua aposta é menor do que o número sorteado.")
else:
    print("Você adivinhou o número sorteado.")