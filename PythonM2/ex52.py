num = int(input('Digite um número:'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m')
        tot = tot + 1
    else:
        print('\033[31m')
    print(f'{c}')
print(f'O número {num} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é primo\033[m')
else:
    print('E por isso ele não é primo\033[m')
    