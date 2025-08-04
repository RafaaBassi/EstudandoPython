"""DESAFIO 0082 -  Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""
valores = []
pares = []
impares = []
valores.append(int(input('Digite um valor: ')))
r = str(input('Quer continuar? [S/N] ')).strip().upper()
while r != 'N':
    valores.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')