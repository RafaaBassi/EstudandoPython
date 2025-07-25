import math
numero=float(input('Digite o ângulo que você deseja:'))
seno=math.sin(math.radians(numero))
cosseno=math.cos(math.radians(numero))
tangente=math.tan(math.radians(numero))
print(f'O ângulo de {numero} tem o SENO de {seno:.2f}')
print(f'O ângulo de {numero} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {numero} tem o TANGENTE de {tangente:.2f}')


