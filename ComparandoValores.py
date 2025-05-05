print('-=' *20)
print('COMPARANDO  VALORES')
print('-=' *20)
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('{} é maior que {}'.format(n2, n1))
else:
    print('{} é igual a {} '.format(n1, n2))