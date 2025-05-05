
print('-' *30)
print('SEQUENCIA DE FIBONANCI')
print('-' *30)
n = int(input('Quantos termos voce quer mostrar? '))
f1 = 0
f2 = 1
print('*' *45)
print(f'{f1} -> {f2} -> ', end=' ')
count = 3

while count <= n:
    f3 = f1 + f2
    print(f'{f3} -> ', end=' ')
    f1 = f2
    f2 = f3
    count += 1
print('FIM')