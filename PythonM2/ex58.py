'''Melhore o jogo do DESAFIO 028 vai 'pensar' em um número entre 0 e 10. Só que agora o jogo o jogador até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
computador = randint(0, 10)
print('Sou seu computador... adivinhe que número estou pensando entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?'))
    palpite = palpite + 1
    if jogador == computador:
        acertou = True
print(f'Acertou com {palpite} tentativas')
