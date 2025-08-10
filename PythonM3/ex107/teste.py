import moeda 
p = float(input('Digite o preço: R$'))
#PARAMETRO metade
print(f'A metade de {p} é {moeda.metade(p)}')
#PARAMETRO dobro
print(f'O dobro de {p} é {moeda.dobro(p)}')
#PARAMETRO aumentar
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')