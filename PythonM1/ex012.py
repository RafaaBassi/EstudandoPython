preço = float(input('Qual é o preço do produto? R$'))
p = preço - (preço * 5 /100)
print('Com o desconto de 5%, você irá pagar {:.2f}'.format(p))