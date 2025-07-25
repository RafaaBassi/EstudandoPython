nome = input("Digite seu nome completo:").strip()
n = nome.split()
print("Primeiro nome", n[0])
print("Último nome", n[len(n)-1])