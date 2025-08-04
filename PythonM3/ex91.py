"""DESAFIO 091 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),#vai escolher um n° de 1 a 6
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6),}
ran = {}
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ran = sorted(jogo.items(), key= itemgetter(1), reverse=True)
#SORTED ordena
print(ran)