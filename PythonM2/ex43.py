peso = float(input('Qual é seu peso? (kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('Parabéns, você está na faixa de peso normal')
elif 25 <= imc < 30:
    print('Você está em sobrepeso')