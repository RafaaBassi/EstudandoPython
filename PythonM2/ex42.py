r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 < r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo')
    if r1 == r2 and r2 == r3:
        print('Equilátero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os segmentos acima \033[4;37mnão\033[m podem formar um triângulo')