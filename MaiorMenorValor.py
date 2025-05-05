n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor :'))
n3 = int(input('Digite o terceiro valor: '))
if n1 > n2 and n1>n3:
    print('O maio valor digitado entre {}, {} e {} foi o numero {}' .format(n1, n2, n3, n1))
elif n2 > n1 and n2 > n3:
    print('O maior valore digitado entre {}, {} e {} foi o numero {}' .format(n1, n2, n3, n2))
else:
    print('O maior valor digitado entre {}, {}, {} foi o numero {}' .format(n1, n2, n3, n3))

if n1 < n2 and n1 < n3:
        print('O menor valor digitado entre {}, {} e {} foi o numero {}'.format(n1, n2, n3, n1))
elif n2 < n1 and n2 < n3:
        print('O menor valor digitado entre {}, {} e {} foi o numero {}'.format(n1, n2, n3, n2))
else:
        print('O menor valor digitado entre {}, {}, {} foi o numero {}'.format(n1, n2, n3, n3))
