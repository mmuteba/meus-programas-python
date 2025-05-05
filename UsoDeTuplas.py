num = (int(input('Digite um numero: ')), int(input('Digite um numero: ')),
       int(input('Digite um numero: ')), int(input('Digite um numero: ')))
print(f'Voce digitou os numeros: {num}')
c = 0
for n in num:
    if n == 9:
        c += 1
print(f'O numero 9 aprereceu {c} vezes')
#print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareceu na {num.index(3) +1}º posiçao')
else:
    print('O numero 3 nao foi digitado!')
print(f'Os valores pares digitados foram: ', end=' ')
for n in num:
    if n % 2 == 0:
        print(f'{n}', end=' ')

