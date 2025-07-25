print('GERADOR DE PA')
print("="*20)
p = int(input('Primeiro termo:'))
r = int(input("Razão:"))
termo = p
c = 1
while c <= 10:
    print(f'{termo}')
    termo += r
    c += 1
print("Fim")
