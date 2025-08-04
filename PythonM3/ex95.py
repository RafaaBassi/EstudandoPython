"""DESAFIO 095 - Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
time = []
while True:
    jogador = {}
    partidas = []
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(tot):
        partidas.append(int(input(f'  Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
        print('Erro! Responda apenas com S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"Cod":<4}{"Nome":<15}{"Gols":<20}{"Total":<5}')
print('-' * 50)
for i, j in enumerate(time):
    print(f'{i:<4}{j["nome"]:<15}{str(j["gols"]):<20}{j["total"]:<5}')
print('-' * 50)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'     No jogo {i + 1} fez {g} gols.')
print('<< VOLTE SEMPRE >>')
