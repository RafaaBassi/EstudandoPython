print("-"*25)
print('Sequência de Fibonacci')
print("-"*25)
n = int(input("Quantos termos você quer? "))
t1 = 0
t2 = 1
print(f'{t1} -> {t2} ', end="") #para não pular linha
c = 3
while c <= n:
    t3 = t1 + t2
    print(f'-> {t3}', end="")
    t1 = t2 
    t2 = t3
    c += 1
print(" -> Fim")