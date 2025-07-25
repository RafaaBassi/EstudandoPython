'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
	- À vista dinheiro/cheque: 10% de desconto
	- À vista no cartão: 5% de desconto 
	- Em até 2x no cartão: preço normal
	- 3x ou mais no cartão: 20% de jiros
'''
print('{:=^40}'.format('LOJAS GUANABARA')) # Ele vai centralizar a palavra no meio de 40(^ significa centralizado)
preco = float(input('Preço das compras: R$'))
print('''Formas de pagamento 
[1] À vista dinheiro/cheque
[2] À vista no cartão 
[3] Em até 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção?'))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc:.2f}x de R${parcela:.2f} COM JUROS')
else:
    total = 0
    print('Erro! Tente novamente')
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final')