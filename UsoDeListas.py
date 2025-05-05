numero = []
maior = 0
menor = 0
for c in range(0, 5):
    numero.append(int(input(f'Digite o numero na posicao {c}: ')))
    if c == 0:
        maior = menor = numero[c]
    else:
        if numero[c] > maior:
            maior = numero[c]
        if numero[c] < menor:
            menor = numero[c]
print('=-' *30)
print(f'Voce digitou os valores {numero}')
print(f'O maior valor digitado foi {maior}, nas posicoes ', end=' ')
for i, v in enumerate(numero):
    if v == maior:
        print(f'{i}...', end=' ')
print(f'\nO menor valor digitado foi {menor}, nas posicoes ', end=' ')
for i, v in enumerate(numero):
    if v == menor:
        print(f'{i}...', end=' ')