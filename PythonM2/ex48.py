'''Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
soma = 0 #---> isso se chama acumulador (somando ou multiplicando um n° no proximo)
cont = 0 #---> isso é um contador 
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont = cont+1
        soma = soma + n
print(f"A soma de todos os {cont} valores é de {soma}")