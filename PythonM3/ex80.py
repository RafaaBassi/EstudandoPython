"""DESAFIO 0080 -  Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""
lista = []
for c in range(0,5):
    n = int(input(f'Digite um valor para a posição {c}: '))
    if c == 0 or n > lista[-1]: # se ele for maior que o último valor
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(f'Os valores em ordem são {lista}')