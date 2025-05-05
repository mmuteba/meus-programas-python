listagem = ('lapis', 50,
            'Borracha', 20,
            'Caderno', 300,
            'Estojo', 400,
            'Transferidor', 150,
            'Mochila', 2000,
            'Canetas', 175,
            'Livro', 1500)
print('=' *40)
for m in range(0, len(listagem)):
    if m % 2 == 0:
        print(f'{listagem[m]:.<30}', end='')
    else:
        print(f'Kz{listagem[m]:>9.2f}')