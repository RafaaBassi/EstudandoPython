"""DESAFIO 0081 -  Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.
"""
valores = []
re = valores.append(int(input('Digite um valor: ')))
r = str(input('Quer continuar? [S/N]')).upper()

while not r == 'N':
    re = valores.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N]')).upper()

if 5 in valores:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
v = len(valores)
print(f'Foi digitado {v} valores')
valores.sort(reverse=True)
print(f'Em ordem decrescente {valores}')