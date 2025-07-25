soma = 0
for c in range(1,8):
    num = int(input(f"Digite o {c} valor:"))
    if num % 2 == 0:
        soma = soma + num
print(f'A soma dor números pares são {soma}')