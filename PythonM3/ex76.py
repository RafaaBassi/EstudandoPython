lis = ('Lápis', 1.35, 'Borracha', 2, 'Caderno', 15.98, 'Estojo', 25, 'Transferindo', 4.20, 'Compasso', 9.99, "Mochila", 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(lis)):
    if pos % 2 == 0:
        print(f'{lis[pos]:30}', end='')
    else:
        print(f'R${lis[pos]:>7.2f}')
