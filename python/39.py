import random

numero = random.randint(1, 10)

aposta = int(input("Insira um número entre 1 e 10: "))

if aposta == numero:
    print("Parabéns, você adivinhou o número!")
else:
    print("Aposta incorreta.")