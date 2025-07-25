'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
sexo = str(input('Qual é seu sexo? [F/M] ')).upper()[0].strip()
while sexo not in "MF":
    print('Erro! Digite novamente')
    sexo = str(input('Qual é seu sexo? [F/M] ')).upper()[0].strip()
print(f"Sexo {sexo} registrado com sucesso")
