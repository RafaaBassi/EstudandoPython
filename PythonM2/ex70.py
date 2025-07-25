total = totmil = menos = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
        if cont == 1:
            menor = preco
            barato = preco
            barato = produto
        else:
            if preco < menor:
                menor = preco
    resp = ''
    while resp not in "SN":
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total foi {total}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato é {barato}, custa R${menor}')
