import random

livros = ["Assassinato no Expresso Oriente", "Cai o Pano", "Noite sem Fim", "E não Sobrou Nenhum"]

numero_gerado = random.randint(1, 4)

sorteio = livros[numero_gerado - 1]

print(sorteio)