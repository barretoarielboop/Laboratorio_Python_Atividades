acessos = [{"usuario1": "123@jkm"}, {"usuario2": "ratshfch"}, {"usuario3": "senhasenha"}]

usuario = input("Insira o nome de usuário:")
senha = input("Insira a senha:")
indice = int(input("Insira o índice do usuário:"))

def acessar(usuario, senha, indice):

    if indice > len(acessos) or indice < 0:
        print("Índice inexistente.")
    elif usuario not in acessos[indice]:
        print("Usuário não registrado.")
    elif senha != acessos[indice][usuario]:
        print("Senha incorreta.") 
    else:
        print("Acesso permitido.")

    return usuario, senha, indice

print(acessar(usuario, senha, indice))