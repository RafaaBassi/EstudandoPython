km = float(input("Qual é a distancia em Km da viajem?"))
if km <= 200:
    print(f"O preço ficará R${km* 0.50}")
else:
    print(f"O preço ficará R${km* 0.45}")