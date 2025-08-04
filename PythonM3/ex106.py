"""DESAFIO 106 - Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
"""
c = ('\033[m', # 0 sem cores
     '\033[0;30;41m', # 1 vermelho
     '\033[0;30;40m', # 2 verde
     '\033[0;30;43m', # 3 amarelo
     '\033[0;30;46m', # 4 azul
     '\033[0;30;45m', # 5 roxo
     '\033[0;37;40m', # 6 branco
     ); 

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f' {msg} ')
    print('~' * tam)
    print(c[0], end='')

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYTHON', 1)
    comando = str(input(f'{c[0]}Função ou Bíblioteca >>')).strip()
    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO', 1)
        break
    else:
        ajuda(comando)
    