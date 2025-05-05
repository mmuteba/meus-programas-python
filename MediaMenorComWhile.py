number = count = soma = media = maior = menor = 0
letra = 'S'
while letra in  'Ss':
    number = int(input('Digite um numero: '))
    count += 1
    soma += number
    if count == 1:
        maior = menor = number
    else:
        if number > maior:
            maior = number
        if number < menor:
            menor = number
    letra = str(input('Quer continuar? [S/N]: '))
media = soma / count
print(f'Voce digitou {count} numeros e a media é de {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')