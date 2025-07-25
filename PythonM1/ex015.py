d = int(input('Quantos dias o carro foi usado?'))
km = float(input('Qual é quantidade de Km percorrido pelo carro alugado?'))
custo = (d*60) + (km*0.15)
print('O custo pelo carro ficará de {: .2f}'.format(custo))