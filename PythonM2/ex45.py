from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2) #faz o computador escolher um número de tal a tal periodo
print('''Suas opções:
[0] PEDRA
[1] PAPEL 
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11) # vai repetir 11 vezes o -=
print(f'Computador jogou {itens[computador]}')

if 0 <= jogador <= 2:
    print(f'Jogador jogou {itens[jogador]}')
else:
    print('Jogador fez uma jogada inválida!')
print('-=' * 11)

if jogador < 0 or jogador > 2:
    print('Jogada inválida.')
elif computador == jogador:
    print('Empate')
elif (computador == 0 and jogador == 1) or \
     (computador == 1 and jogador == 2) or \
     (computador == 2 and jogador == 0):
    print('Jogador vence')
else:
    print('Computador vence')