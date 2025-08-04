"""DESAFIO 096 - Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno."""
def area(a, b):
    c = a*b
    print(f'A área vai ser de {c}')

a= float(input('LARGURA (m):'))
b= float(input('COMPRIMENTO (m):'))
area(a, b)