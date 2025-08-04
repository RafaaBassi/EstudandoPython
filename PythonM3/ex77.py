palavras = ('aprender', 'programas', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado','programador','futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='') #\n para quebrar linha
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')