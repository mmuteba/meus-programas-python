num = int(input('Digite um numero para ver sua tabuada: '))
print('=-=', end=' ')
print('TABUADA', end=' ')
print('=-=')
for count in range (1, 11):
    resultado = num * count
    print('{} x {} = {}' .format(num, count, resultado))
print('=-=' *5)