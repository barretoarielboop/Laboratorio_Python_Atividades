def animais(a, b):
    total = a*4
    pernas_faltando = total - b
    total_galinhas = pernas_faltando/2
    total_coelhos = a-total_galinhas
    return total_coelhos
    return total_galinhas

print(animais(35,94))
print(35-(animais(35,94)))