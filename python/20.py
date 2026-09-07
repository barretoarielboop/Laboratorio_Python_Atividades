notas = []

numeros= int(input("Digite uma nota: "))

while numeros != 0:
    notas.append(numeros)
    numeros = int(input("Digite uma nota: "))

total = sum(notas)
print(total)