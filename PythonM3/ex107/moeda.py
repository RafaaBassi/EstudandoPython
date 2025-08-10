def aumentar(preco, taxa):#PARAMETRO aumentar
    res = preco + (preco * taxa/100)
    return res

def diminuir(preco, taxa): #PARAMETRO diminuir
    res = preco - (preco * taxa/100)
    return res

def dobro(preco): #PARAMETRO dobro
    res = preco * 2
    return res

def metade(preco): #PARAMETRO metade
    res = preco /2
    return res