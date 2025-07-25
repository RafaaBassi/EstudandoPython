"""
num = int(input("Digite um número:"))
n = str(num)
print("Analisando o número")
print("Unidade", n[3])
print("Dezena ", n[2])
print("Centena", n[1])
print("Milhar", n[0])"""
num = int(input("Digite um número:"))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"Unidade{u}")
print(f"Dezena {d}")
print(f"Centena {c}")
print(f"Milhar {m}")