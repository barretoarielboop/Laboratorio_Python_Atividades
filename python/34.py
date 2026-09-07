alunos = {"João": 6.5, "Maria": 7.1, "José": 8.5}

consulta = input("Digite o nome do aluno a ser consultado: ")

if consulta in alunos:
    print(alunos[consulta])
else:
    print("Aluno não encontrado")