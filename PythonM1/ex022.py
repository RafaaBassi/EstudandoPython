""" Crie um programa que leia o nome completo de uma pessoa e mostre:
1. O nome com todas as letras maiúsculas 
2.O nome com todas minúsculas 
3.Quantas letras ao todo sem considerar espaços
 4.Quantas letras tem o primeiro nome.
"""
nome = input("Digite seu nome completo:")
print(nome.upper())
print(nome.lower())
print(len(nome.strip()))
print(nome.split()[0])