"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO' """
n = input("Qual é a cidade que vc nacsceu?")
var = n.strip().upper()
resultado = "SANTO" in var
print(resultado)