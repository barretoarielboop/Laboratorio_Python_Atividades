codigos = [1111, 2222, 3333, 4444]

entrada = int(input("Insira o código: "))
if entrada in codigos:
    print("Código válido")
else:
    print("Código inválido.")