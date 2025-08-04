"""DESAFIO 105 - Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas             – A menor nota
– A média da turma                  – A situação (opcional)"""

def notas(*n, sit=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >=7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)