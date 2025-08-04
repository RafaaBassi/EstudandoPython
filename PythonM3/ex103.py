"""DESAFIO 102 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""
def gol(a='<descolhecido>', b=0):
    print(f'O jogador {a} fez {b} gol/s no campeonato.')

A = str(input('Nome do Jogador: '))
B = str(input('Número de gols: '))
if B.isnumeric():
    B = int(B)
else:
    B = 0
if A.strip() == "":
    gol(b=B)
else:
    gol(A, B)
