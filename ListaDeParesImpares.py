lista = []
pares = []
ímpares = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)
print('=+=' *20)
print(f'A lista completa é {lista}')
print(f'A lista e pares é {pares}')
print(f'A lista de ímpares é {ímpares}')