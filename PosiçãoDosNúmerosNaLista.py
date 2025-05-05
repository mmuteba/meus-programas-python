lista = []

for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            print(f'Adicionado na posicao {pos} da lista...')
            pos += 1
print('=*' *20)
print(f'Os numeros digitados foram: {lista}')