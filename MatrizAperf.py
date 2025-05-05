matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
valor = 0
soma = somColuna =  maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite os valores [{l}, {c}]: '))
        matriz[l][c] = valor
        if valor % 2 == 0:
            soma += valor
        if c == 2:
            somColuna += valor
        if l == 1:
            if valor > maior:
                maior = valor
            else:
                maior = maior
print('+=' *20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('+=' *20)
print(f'A soma de todos os valores pares é: {soma}')
print(f'A soma dos valores da terceira coluna é: {somColuna}')
print(f'O maior valor da segunda linha é: {maior}')