"""Faça um programa que leia uma frase pelo teclado e mostre: 
1.Quantas vezes aparece a letra A 
2.Em que posição ela aparece a primeira vez
3.Em que posição aparece na última vez.
"""
frase = input("Digite uma frase:").upper().strip()
print(f"Letra A aparece {frase.count('A')} vezes")
print(f"Primeira vez que A aparece {frase.find('A')+1} vezes")
print(f"Última vez que A aparece {frase.rfind('A')+1} vezes")