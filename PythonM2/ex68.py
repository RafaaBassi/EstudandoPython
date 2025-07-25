from random import randint
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você perdeu')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')