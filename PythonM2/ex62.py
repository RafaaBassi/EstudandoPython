print('GERADOR DE PA')
print("="*20)
p = int(input('Primeiro termo:'))
r = int(input("Razão:"))
termo = p
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(f"{termo}")
        termo += r
        c += 1
    print("Pausa")
    mais = int(input('Quantos termos você quer mostras a mais?'))
print("Fim")