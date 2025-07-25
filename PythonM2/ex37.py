num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[1] converter para binário
[2] converter para octal 
[3] converter para hexadecimal''')
opcao = int(input('Sua opção:'))
if opcao == 1:
    print(f'{num} convertido para binário é igual a {bin(num) [2:]}')
elif opcao == 2:
    print(f'{num} convertido para octal é igual a {oct(num) [2:]}')
elif opcao == 3:
    print(f'{num} convertido para hexadecimal é igual a {hex(num) [2:]}')
else:
    print('Opção inválida. Tente novamente')