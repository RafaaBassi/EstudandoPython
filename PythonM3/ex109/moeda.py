def aumentar(preco=0, taxa=0, formato=False):#PARAMETRO aumentar
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preco=0, taxa=0, formato=False): #PARAMETRO diminuir
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preco=0, formato=False): #PARAMETRO dobro
    res = preco * 2
    return res if formato is False else moeda(res)

def metade(preco=0, formato=False): #PARAMETRO metade
    res = preco /2
    return res if formato is False else moeda(res)

def moeda(preco = 0, moeda = 'R$'): #PARAMETRO R$
    return f'{moeda}{preco}'.replace('.', ',')
