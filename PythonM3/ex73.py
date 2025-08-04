bra = (
"Flamengo", "Palmeiras", "Atlético-MG", "São Paulo", "Grêmio",
"Internacional", "Fluminense", "Fortaleza", "Athletico-PR", "Cruzeiro",
"Corinthians", "Botafogo", "Cuiabá", "Bahia", "Vasco",
"Santos", "Bragantino", "Goiás", "Coritiba", "América-MG"
)
print(f'{'='*80}')
print(bra[0:6]) #A
print(f'{'='*80}')
print(bra[-4:]) #B
print(f'{'='*80}')
print(sorted(bra)) #C
print(f'{'='*80}')
print(f'{bra.index('Corinthians')+1}') #D
print(f'{'='*80}')
