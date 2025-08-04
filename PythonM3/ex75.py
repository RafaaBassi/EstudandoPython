n = (int(input("Digite um número:")), int(input("Digite um número:")), int(input("Digite um número:")), int(input("Digite um número:")))
print(f'Você digitou os valores {n}')
print(f'o 9 apareceu {n.count(9)}')
if 3 in n:
    print(f'O 3 está na posição {n.index(3)+1}')
else:
    print('O valor 3 não foi digitado')
for num in n:
    if num % 2 == 0:

        print(num, end='')