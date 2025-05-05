palavras = ('aprender', 'programar', 'linguagem', 'phyton', 'curso', 'gratis', 'estududar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for letra in palavras:
    print(f'\n Na palavra {letra.upper()}, temos: ', end=' ')
    for v in letra:
        if v.lower() in 'aeiou':
            print(f'{v}', end=' ')