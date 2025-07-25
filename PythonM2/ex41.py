'''	- Até 9 anos: MIRIM
	- Até 14 anos: INFANTIL
	- Até 19 anos: JUNIOR
	- Até 20 anos: SÊNIOR
	- Acima: MASTER'''
from datetime import date 
atual = date.today().year
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc
print(f"O atleta tem {idade}")
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
     print('Classificação: INFANTIL')
elif idade <= 19:
      print('Classificação: JUNIOR')
elif idade <= 19:
      print('Classificação: SÊNIOR')
else:
      print('Classificação: MASTER')