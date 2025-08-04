"""DESAFIO 0089 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""
alunos = []
while True:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])

    continuar = input("Deseja continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break
print("\n{:<5} {:<20} {:<10}".format("Nº", "Nome", "Média"))
print("-" * 40)
for i, aluno in enumerate(alunos):
    print("{:<5} {:<20} {:<10.2f}".format(i, aluno[0], aluno[2]))
while True:
    opcao = input("\nMostrar notas de qual aluno? (Digite o número ou '999' para sair): ")
    if opcao == '999':
        break
    elif opcao.isdigit() and int(opcao) < len(alunos):
        indice = int(opcao)
        print(f"Notas de {alunos[indice][0]}: {alunos[indice][1]}")
    else:
        print("Número inválido. Tente novamente.")
