def validar():
    while True:
        try:
            idade = int(input("Digite sua idade:"))
        except ValueError:
            print("Por favor, insira um valor numérico inteiro.")
        else:
            break
    
    return idade

idade = validar()
print(idade)