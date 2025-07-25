somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
for c in range(1, 5):
    print('{:=^40}'.format(f' {c}ª PESSOA '))
    nome = input('Nome: ')
    idade = int(input('Idade: '))  # Corrigido para converter para inteiro
    sexo = input('Sexo [F/M]: ').strip().upper()  # Padroniza para maiúscula
    
    somaidade += idade

    if c == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    elif sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

mediaidade = somaidade / 4
print(f'\nA média de idade do grupo é de {mediaidade:.1f} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
