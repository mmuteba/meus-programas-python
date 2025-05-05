'''lista = []
count = 0
while True:
    n = int(input('Digite um número: '))
    if count == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no principio da lista....')
    else:
        pos = 0
        while n < lista[pos]:
            lista.insert(pos, n)
            break
    count += 1
    pergunta = str(input('Quer continuar ? [S/N] ')).strip().upper()
    if pergunta in 'NS':
        if pergunta == 'N':
            break
print('=*=' *25)
print(f'Voce digitou {count} elementos...')
print(f'Os valores em ordem decrescente sao {lista}')'''
valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar ? [N/S] ')).strip().upper()
    if resp in 'N':
        break
print(f'Voce digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente da lista sao {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 nao faz parte da lista')