"""DESAFIO 102 - Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""
def fatorial(n, show=False):
    """ -> Calcula o fatorial de um número
    n: O número a ser calculado
    i: O número que o usuário colocou
    show: (opcional) Mostrar ou não a conta
    return: O valor do fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


i = int(input('Digite um número: '))
print(fatorial(i, show=True)) #True: faz com que tenha a conta no terminal
#False: Só vai aparecer o resultado
# TESTE DO HELP: help(fatorial)