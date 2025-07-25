'''Crie um programa que leia dois valores e mostre um menu na tela:
1.soma
2.multiplicar
3.maior
4.novos números
5.sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
n1 = int(input("Digite o primeiro valor:"))
n2 = int(input('Digite o segundo valor:'))
p = 0
while p != 5:
    print(""" 
    [1].soma
    [2].multiplicar
    [3]. qual é o n° maior
    [4].novos números
    [5].sair do programa""")
    p = int(input(">>> O que você quer fazer?"))
    if p == 1:
        print(f"{n1} + {n2} = {n1+n2}")
    elif p == 2:
        print(f"{n1} x {n2} = {n1*n2}")
    elif p == 3:
        if n1 > n2:
            print(f"{n1} é maior")
        else:
            print(f"{n2} é maior")
    elif p == 4:
        print("Digite os números novamente")
        n1 = int(input("Primeiro valor:"))
        n2 = int(input('Segundo valor:'))
    elif p == 5:
        print("Finalizando...")
    else:
        print("Opção inválida. Tente novamente")
print('Fim!')