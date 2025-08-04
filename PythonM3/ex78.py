"""DESAFIO 0078 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
valores = []
maior = 0
menor = 0
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont} ')))
    if cont ==0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior: #Se o valor que digitei for maior que minha variáver MAIOR, então substitua ele
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print(f'Você digitou os valores {valores}')
print(f'O maior número digitado foi {maior} na posição ',end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print(f'O menos número digitado foi {menor} na posição ',end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')